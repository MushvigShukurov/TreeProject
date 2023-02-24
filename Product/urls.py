from django.urls import path, include
from Product.views import index
urlpatterns = [
    path('',index,name="home-page"),
    path('api/', include('Product.api.urls')),
]