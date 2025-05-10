import base64
from io import BytesIO

import pyotp
import qrcode
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class TwoFASetupView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if not user.otp_secret:
            user.otp_secret = pyotp.random_base32()
            user.save()

        otp_uri = pyotp.totp.TOTP(user.otp_secret).provisioning_uri(
            name=user.email, issuer_name="DeltaFleet"
        )

        # Generate QR Code
        qr = qrcode.make(otp_uri)
        buf = BytesIO()
        qr.save(buf, format='PNG')
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')

        return Response({
            "otp_secret": user.otp_secret,
            "qr_code_base64": image_base64
        })


class TwoFAVerifyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        otp_code = request.data.get('otp_code')

        if not otp_code:
            return Response({"detail": "OTP code is required."}, status=status.HTTP_400_BAD_REQUEST)

        totp = pyotp.TOTP(user.otp_secret)
        if totp.verify(otp_code):
            user.is_2fa_enabled = True
            user.save()
            return Response({"detail": "2FA enabled successfully."})
        return Response({"detail": "Invalid OTP code."}, status=status.HTTP_400_BAD_REQUEST)

class TwoFADisableView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        otp_code = request.data.get('otp_code')

        if not otp_code:
            return Response({"detail": "OTP code is required to disable 2FA."}, status=status.HTTP_400_BAD_REQUEST)

        totp = pyotp.TOTP(user.otp_secret)
        if totp.verify(otp_code):
            user.is_2fa_enabled = False
            user.otp_secret = None
            user.save()
            return Response({"detail": "2FA disabled successfully."})
        return Response({"detail": "Invalid OTP code."}, status=status.HTTP_400_BAD_REQUEST)
