from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from .permissions import IsAuthenticatedAndAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    """Представление для работы с постами."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedAndAuthorOrReadOnly]

    def perform_create(self, serializer):
        """Выполняет создание новой записи."""
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    """Представление для работы с группами."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    """Представление для работы с комментариями к постам."""

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedAndAuthorOrReadOnly]

    def get_queryset(self):
        """Ensure the post exists and return comments for it."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments.all()  # Assuming 'comments' is the related_name

    def perform_create(self, serializer):
        """Ensure the post exists before creating a comment."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
