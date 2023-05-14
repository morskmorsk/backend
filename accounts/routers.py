from rest_framework.routers import DefaultRouter
from .api_views import CustomUserViewSet

router = DefaultRouter()
router.register(r'', CustomUserViewSet)
