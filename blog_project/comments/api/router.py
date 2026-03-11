from rest_framework.routers import DefaultRouter
from .views import CommentApiViewSet

router_comment = DefaultRouter()
router_comment.register(prefix='comments', viewset=CommentApiViewSet, basename='comment')