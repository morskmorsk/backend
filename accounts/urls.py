from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('users/new/', CustomUserViewSet.as_view({'post': 'create'}),
    #      name='user-register'),
]
