"""Imports."""
from django.apps import AppConfig


class PostsConfig(AppConfig):
    """Конфигурация приложения Django для управления постами."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
