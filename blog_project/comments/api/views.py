from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.permissions import IsOwnerOrReadOnly

class CommentApiViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['created_at']
    filterset_fields = ['post']
    