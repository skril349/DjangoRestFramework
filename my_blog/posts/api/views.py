import re

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from posts.models import Post
from posts.api.serializers import PostSerializer



class PostModelViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    


# class PostViewSet(ViewSet):
    
#     # get /api/posts
#     def list(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
    
#     # get /api/posts/{id}
#     def retrieve(self, request, pk=int):
#         try:
#             post = PostSerializer(Post.objects.get(id=pk))
#             return Response(status=status.HTTP_200_OK, data=post.data)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Post not found'})

#     # post /api/posts
#     def create(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED, data=serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    
    
# class PostApiView(APIView):
#     def get(self, request):
#         serializer = PostSerializer(Post.objects.all(), many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED, data=serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        


        
