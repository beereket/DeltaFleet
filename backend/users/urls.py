from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView,
    DriverApplicationCreateView,
    DriverApplicationListView,
    DriverApplicationDecisionView, VerifyEmailView, TwoStepLoginView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TwoStepLoginView, name='login'),
    path('verify-email/<uidb64>/<token>/', VerifyEmailView.as_view(), name='verify-email'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('driver/apply/', DriverApplicationCreateView.as_view(), name='driver-apply'),
    path('driver/forms/', DriverApplicationListView.as_view(), name='driver-forms'),
    path('driver/forms/<int:pk>/<str:decision>/', DriverApplicationDecisionView.as_view(), name='driver-decision'),
]
