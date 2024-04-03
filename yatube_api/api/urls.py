"""Imports."""
from django.urls import include, path

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('v1/posts', PostViewSet, basename='post')
router_v1.register('v1/groups', GroupViewSet, basename='group')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='v1-post-comments')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
