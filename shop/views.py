from django.shortcuts import render
from .models import Product

def index(request):
    product_objects = Product.objects.all()
    context = {'product_objects': product_objects}
    return render(request, 'shop/index.html', context)
