from rest_framework import routers
from .views import TagViewSet, GroupViewSet, ImageViewSet, AlertViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'images', ImageViewSet, basename='image')
router.register(r'alerts', AlertViewSet, basename='alert')
