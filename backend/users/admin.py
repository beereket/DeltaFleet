from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, DriverApplication

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_email_verified', 'is_2fa_enabled', 'is_staff')
    list_filter = ('role', 'is_email_verified', 'is_2fa_enabled', 'is_staff')
    search_fields = ('username', 'email')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role', 'is_email_verified', 'is_2fa_enabled', 'otp_secret')}),
    )
    readonly_fields = ('otp_secret',)


@admin.register(DriverApplication)
class DriverApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'license_number', 'experience_years', 'status', 'submitted_at')
    list_filter = ('status', 'submitted_at')
    search_fields = ('user__username', 'license_number')
    readonly_fields = ('submitted_at',)
