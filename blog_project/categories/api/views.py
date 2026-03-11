from codecs import lookup

from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from categories.models import Category
from categories.api.permissions import IsAdminOrReadOnly

class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    #queryset = Category.objects.all()
    queryset = Category.objects.filter(published=True) #solo mostrar categorias publicadas
    lookup_field = 'slug' #buscar por slug en lugar de id
    