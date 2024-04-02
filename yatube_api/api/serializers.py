"""Imports."""
from posts.models import Comment, Group, Post
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group."""

    class Meta:
        """Внутренний класс для определения настроек сериализатора модели."""

        model = Group
        fields = ['id', 'title', 'slug', 'description']


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post."""

    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        """Внутренний класс для определения настроек сериализатора модели."""

        model = Post
        fields = ['id', 'text', 'pub_date', 'author', 'image', 'group']


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment."""

    author = serializers.SerializerMethodField()

    class Meta:
        """Внутренний класс для определения настроек сериализатора модели."""

        model = Comment
        fields = ['id', 'author', 'post', 'text', 'created']
        read_only_fields = ['author', 'post']

    def get_author(self, obj):
        """Возвращает имя пользователя-автора объекта."""
        return obj.author.username