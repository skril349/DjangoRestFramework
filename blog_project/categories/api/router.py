from rest_framework.routers import DefaultRouter
from .views import CategoryApiViewSet

router_categories = DefaultRouter()
router_categories.register(prefix='categories', viewset=CategoryApiViewSet, basename='categories')