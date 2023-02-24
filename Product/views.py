from django.shortcuts import render
from django.core.exceptions import BadRequest
from Category.models import Category
from Product.models import Product
# Create your views here.

def index(request):
    if request.method == "GET":
        categories = Category.objects.filter(parent_category=None)
        products = Product.objects.all()
        data = {
            'categories':categories,
            'products':products,
        }
        return render(request,'index.html',context=data)
    else:
        return BadRequest("İcazəsiz İstək")