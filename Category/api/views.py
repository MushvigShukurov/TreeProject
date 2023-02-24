# Models
from Category.models import Category

# Serializers
from Category.api.serializers import CategorySerializer

# Tools
from rest_framework import generics

# Permission Class
from Category.api.permissions import IsAdminOrReadOnly

class CategoryCreateOrList_APIView(generics.ListCreateAPIView):
    queryset = Category.objects.filter(parent_category=None)
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
