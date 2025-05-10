from io import BytesIO

import pyotp
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model, authenticate
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from config import settings
from .models import DriverApplication
from .utils import email_verification_token
from .serializers import (
    UserRegisterSerializer,
    DriverApplicationSerializer,
    DriverApplicationDecisionSerializer
)
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserRegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        self.send_verification_email(user)

    def send_verification_email(self, user):
        from django.utils.http import urlsafe_base64_encode
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = email_verification_token.make_token(user)
        verify_url = f"http://localhost:8000/api/verify-email/{uid}/{token}/"

        send_mail(
            'Verify Your Email - DeltaFleet',
            f'Hi {user.username},\nPlease verify your email by clicking the link: {verify_url}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
class TwoStepLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        otp_code = request.data.get('otp_code')  # Optional, for second step

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        if user.is_2fa_enabled:
            if not otp_code:
                return Response({"requires_2fa": True}, status=status.HTTP_200_OK)
            totp = pyotp.TOTP(user.otp_secret)
            if not totp.verify(otp_code):
                return Response({"detail": "Invalid OTP code."}, status=status.HTTP_400_BAD_REQUEST)

        # Success → Generate tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        })
class VerifyEmailView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user and email_verification_token.check_token(user, token):
            user.is_email_verified = True
            user.save()
            return Response({"detail": "Email verified successfully."})
        return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

class DriverApplicationCreateView(generics.CreateAPIView):
    queryset = DriverApplication.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DriverApplicationSerializer

    def perform_create(self, serializer):
        if self.request.user.role != 'GUEST':
            return Response({'detail': 'Only GUEST users can apply.'}, status=status.HTTP_403_FORBIDDEN)
        serializer.save(user=self.request.user)

class DriverApplicationListView(generics.ListAPIView):
    queryset = DriverApplication.objects.filter(status='PENDING')
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DriverApplicationSerializer

    def get_queryset(self):
        if self.request.user.role in ['MANAGER', 'ADMIN']:
            return super().get_queryset()
        return DriverApplication.objects.none()

class DriverApplicationDecisionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk, decision):
        if request.user.role not in ['MANAGER', 'ADMIN']:
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        try:
            app = DriverApplication.objects.get(pk=pk, status='PENDING')
        except DriverApplication.DoesNotExist:
            return Response({'detail': 'Application not found or already processed.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = DriverApplicationDecisionSerializer(data=request.data)
        if serializer.is_valid():
            app.status = 'APPROVED' if decision == 'approve' else 'DENIED'
            app.manager_response = serializer.validated_data.get('manager_response', '')
            app.save()

            if decision == 'approve':
                app.user.role = 'DRIVER'
                app.user.save()

            return Response({'detail': f'Application {app.status}.'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
