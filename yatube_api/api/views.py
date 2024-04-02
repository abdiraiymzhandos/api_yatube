"""Imports."""
from posts.models import Comment, Group, Post
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Представление для работы с постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Выполняет создание новой записи."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """Представление для работы с группами."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def create(self, request, *args, **kwargs):
        """Обрабатывает попытки создания новой группы через API."""
        return Response({'detail': 'Method "POST" not allowed.'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для работы с комментариями к постам."""

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def get_queryset(self):
        """Возвращает набор данных для конкретного комментария."""
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post=post_id)

    def perform_create(self, serializer):
        """Выполняет создание комментария."""
        post_id = self.kwargs.get('post_id')
        post = Post.objects.get(id=post_id)
        serializer.save(author=self.request.user, post=post)
