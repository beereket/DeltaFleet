from django.urls import path
from .views import TripListCreateView

urlpatterns = [
    path('trips/', TripListCreateView.as_view(), name='trip-list-create'),
    path('assign_trip_to_driver/<int:driver_id>/', views.assign_trip_to_driver, name='assign_trip_to_driver'),
]
