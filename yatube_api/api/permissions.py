"""Imports."""
from rest_framework import permissions


class IsAuthenticatedAndAuthorOrReadOnly(permissions.BasePermission):
    """Пользовательский класс разрешений.

    который позволяет объектам быть редактируемыми только их авторами.
    """

    def has_permission(self, request, view):
        """Проверяем, аутентифицирован ли пользователь."""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Определяет, имеет ли пользователь разрешение на.

        выполнение операции с объектом.
        """
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
