from rest_framework.serializers import ModelSerializer
from comments.models import Comment
from posts.api.serializers import PostSerializer
from users.api.serializers import UserSerializer

class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'post', 'user']