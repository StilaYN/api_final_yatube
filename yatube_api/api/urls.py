from django.urls import include, path
from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments')
router.register(r'follow', FollowViewSet)


urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls))
]
