from django.urls import path 
from Product.api.views import ProductCreateOrList_APIView, ProductDetailAPIView
urlpatterns = [
    path('all/',ProductCreateOrList_APIView.as_view(),name="products"),
    path('detail/<int:pk>',ProductDetailAPIView.as_view(),name="product-detail")
]