from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        fields = ("id", "author", "text", "pub_date", "image", "group")
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        slug_field="username",
        read_only=True,
    )

    class Meta:
        fields = (
            "id",
            "author",
            "post",
            "text",
            "created",
        )
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(
        slug_field="username",
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = "__all__"
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=("user", "following"),
            )
        ]

    def validate(self, data):
        if self.context["request"].user == data["following"]:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        return data
