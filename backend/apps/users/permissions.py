from rest_framework import permissions
from .models import Role

# Роль Admin
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.ADMIN

# Роль Manager
class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.MANAGER

# Роль Driver
class IsDriver(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.DRIVER

# Роль Patient (например для медицинских приложений)
class IsPatient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.PATIENT

# Роль Doctor (Surgeon, Rehabilitator)
class IsDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [Role.SURGEON, Role.REHABILITATOR]

# Роль Surgeon
class IsSurgeon(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.SURGEON

# Роль Rehabilitator
class IsRehabilitator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.REHABILITATOR

# Администратор или Доктор
class IsAdminOrDoctor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in [Role.ADMIN, Role.REHABILITATOR, Role.SURGEON]

# Проверка, является ли пользователь владельцем объекта или администратором
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.role == Role.ADMIN

# Условие для админа, чтобы только он мог добавлять других администраторов
class IsAdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.ADMIN
