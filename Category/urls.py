from django.urls import path, include

urlpatterns = [
    path("api/",include("Category.api.urls")),
]