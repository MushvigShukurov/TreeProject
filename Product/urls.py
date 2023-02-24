from django.urls import path
from Product.views import index
urlpatterns = [
    path('',index,name="home-page"),
]