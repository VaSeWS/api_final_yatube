from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()

router.register(
    r"posts/(?P<post_id>\d+)/comments",
    CommentViewSet,
    basename="comments"
)
router.register(
    r"posts",
    PostViewSet,
)
router.register(
    r"follow",
    FollowViewSet,
    basename="follow"
)
router.register(
    r"groups",
    GroupViewSet,
)

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
