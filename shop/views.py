from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from django.shortcuts import redirect


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

def login_views(request):
    form = LoginForm()

    return render(request,'shop/ajouter.html')

def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(title__icontains=query)
    return render(request, 'shop/search_results.html', {'results': results, 'query': query})

def some_view(request):
    cart = request.session.get('cart', {})  # ex: {'product_id': quantity, ...}
    cart_count = sum(cart.values())  # total des quantités
    # Puis passer dans le contexte
    return render(request, 'template.html', {'cart_count': cart_count})

def cart_detail(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())
    
    cart_items = []
    total = 0
    for product in products:
        quantity = cart[str(product.id)]
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'shop/cart_detail.html', {
        'cart_items': cart_items,
        'total': total
    })
def produits_par_categorie(request, categorie_id):
    categorie = get_object_or_404(Category, id=categorie_id)
    produits = Product.objects.filter(category=categorie)
    return render(request, 'shop/produits_par_categorie.html', {
        'categorie': categorie,
        'produits': produits
    })

 
 # views.py


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))  # redirige vers la page précédente



def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        del cart[product_id_str]
        request.session['cart'] = cart
    return redirect('cart_detail')


