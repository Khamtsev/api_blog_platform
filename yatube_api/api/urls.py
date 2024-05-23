from rest_framework.routers import SimpleRouter

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, FollowViewSet, PostViewSet

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register('groups', GroupViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
