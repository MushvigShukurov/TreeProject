from rest_framework import generics
from Product.models import Product
from Product.api.serializers import ProductSerializer
from Product.api.permissions import IsAdminOrReadOnly

class ProductCreateOrList_APIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
