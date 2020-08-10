from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)

from . import views


router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='post')
router.register(
    r'posts/(?P<post_id>\d+)/comments', 
    views.CommentViewSet, 
    basename='comment'
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('group/', views.GroupViewSet.as_view(), name='group'),
    path('follow/', views.FollowViewSet.as_view(), name='follow'),
    path('', include(router.urls))
]
