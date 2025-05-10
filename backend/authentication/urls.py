from django.urls import path

from .views import TwoFASetupView, TwoFAVerifyView, TwoFADisableView

urlpatterns = [
    path('2fa/setup/', TwoFASetupView.as_view(), name='2fa-setup'),
    path('2fa/verify/', TwoFAVerifyView.as_view(), name='2fa-verify'),
    path('2fa/disable/', TwoFADisableView.as_view(), name='2fa-disable'),
]