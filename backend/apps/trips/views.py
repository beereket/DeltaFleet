from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Trip
from .serializers import TripSerializer
from rest_framework.permissions import IsAuthenticated

class TripListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
