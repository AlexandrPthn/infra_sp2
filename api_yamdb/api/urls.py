from django.urls import include, path
from rest_framework import routers

from api.views import (CategoryViewSet, GenreViewSet, TitleViewSet,
                       ReviewViewSet, CommentViewSet, UsersViewSet,
                       APIGetToken, APISignup)


router = routers.DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

auth_urlpatterns = [
    path('token/', APIGetToken.as_view(), name='get_token'),
    path('signup/', APISignup.as_view(), name='signup'),
]

urlpatterns = [
    path('v1/auth/', include(auth_urlpatterns)),
    path('v1/', include(router.urls)),
]
