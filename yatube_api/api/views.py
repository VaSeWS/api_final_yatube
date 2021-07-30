from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions, filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Comment, Follow, Group, Post
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class CreateListViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class ListRetrieveViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Изменение чужого контента запрещено!"
            )
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Изменение чужого контента запрещено!"
            )
        super().perform_destroy(instance)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)

        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Изменение чужого контента запрещено!"
            )
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                "Изменение чужого контента запрещено!"
            )
        super().perform_destroy(instance)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ("following__username",)

    def get_queryset(self):
        user = self.request.user

        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(ListRetrieveViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
