from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer
from rest_framework.filters import  OrderingFilter
#from posts.api.permissions import IsAdminOrReadOnly

class CommentApiViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_at']
    #permission_classes = [IsAdminOrReadOnly]