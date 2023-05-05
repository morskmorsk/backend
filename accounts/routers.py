from rest_framework.routers import DefaultRouter
from .api import CustomUserViewSet

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)
