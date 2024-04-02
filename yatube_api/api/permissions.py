"""Imports."""
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """Право доступа, позволяющее авторам объекта выполнять изменения."""

    def has_object_permission(self, request, view, obj):
        """Определяет, имеет ли пользователь разрешение на."""
        """выполнение операции с объектом"""
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
