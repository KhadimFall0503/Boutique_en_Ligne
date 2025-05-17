from django.shortcuts import render,get_object_or_404
from .models import Product

def index(request):
    product_objects = Product.objects.all()
    context = {'product_objects': product_objects}
    return render(request, 'shop/index.html', context)

def liste_produits(request):
    produits = Product.objects.all()
    context = {'produits':produits}
    return render (request, 'shop/liste_produits.html', context)

def detail_produits(request,id):
    detail = get_object_or_404(Product,id=id)
    context = {'detail':detail}
    return render(request,'shop/detail_produits.html',context)
