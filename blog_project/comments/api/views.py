from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer
#from posts.api.permissions import IsAdminOrReadOnly

class CommentApiViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    #permission_classes = [IsAdminOrReadOnly]