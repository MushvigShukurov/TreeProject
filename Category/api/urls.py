from django.urls import path 
from Category.api.views import CategoryCreateOrList_APIView, CategoryDetailAPIView
urlpatterns = [
    path('all/',CategoryCreateOrList_APIView.as_view(),name="api-categories"),
    path('detail/<int:pk>',CategoryDetailAPIView.as_view(),name="category-detail"),
]