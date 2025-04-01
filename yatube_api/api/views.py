from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import exceptions
from posts.models import Group, Post
from .serializers import GroupSerializer, PostSerializer
from rest_framework import pagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset =  Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied('Изменение чужого контента запрещено!')
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied('Удаление чужого контента запрещено!')
        super().perform_destroy(instance)
