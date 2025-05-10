from rest_framework import serializers


class TwoFAVerificationSerializer(serializers.Serializer):
    otp_code = serializers.CharField()
