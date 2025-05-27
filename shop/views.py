from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Product, Category
from .forms import ProductForm

# Page d'accueil
def index(request):
    product_objects = Product.objects.all()[:8]
    context = {'product_objects': product_objects}
    return render(request, 'shop/index.html', context)

# Liste des produits
def liste_produits(request):
    produits = Product.objects.all()
    context = {'produits': produits}
    return render(request, 'shop/liste_produits.html', context)

# Vérifie si l'utilisateur est superuser (admin)
def is_superuser(user):
    return user.is_superuser

# Ajouter un produit (réservé aux superusers)
@login_required
@user_passes_test(is_superuser)
def ajouter_produit(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Produit ajouté avec succès.")
            return redirect('liste_produits')
    else:
        form = ProductForm()
    return render(request, 'shop/ajouter_produit.html', {'form': form})

# Détail d'un produit
def detail_produits(request, id):
    detail = get_object_or_404(Product, id=id)
    context = {'detail': detail}
    return render(request, 'shop/detail_produits.html', context)

# Résultats de recherche
def search_results(request):
    query = request.GET.get('q')
    results = Product.objects.filter(title__icontains=query) if query else []
    return render(request, 'shop/search_results.html', {'results': results, 'query': query})

# Détail du panier
def cart_detail(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0
    for product in products:
        quantity = cart.get(str(product.id), 0)
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

# Produits par catégorie
def produits_par_categorie(request, categorie_id):
    categorie = get_object_or_404(Category, id=categorie_id)
    produits = Product.objects.filter(category=categorie)
    return render(request, 'shop/produits_par_categorie.html', {
        'categorie': categorie,
        'produits': produits
    })

# Ajouter un produit au panier
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    request.session['cart'] = cart
    return redirect(request.META.get('HTTP_REFERER', 'liste_produits'))

# Supprimer un produit du panier
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart_detail')

# Ajouter un produit par un utilisateur authentifié (non superuser)
@login_required
def ajouter_produit_utilisateur(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            produit = form.save(commit=False)
            produit.user = request.user  # Assure que Product a un champ user
            produit.save()
            messages.success(request, "Produit ajouté avec succès.")
            return redirect('liste_produits')
    else:
        form = ProductForm()

    return render(request, 'shop/ajouter_produit_utilisateur.html', {'form': form})

# Page de connexion dédiée aux superusers (modal ou page spécifique)
def superuser_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            messages.success(request, "Connecté en tant que superuser.")
            return redirect('ajouter_produit_utilisateur')
        else:
            messages.error(request, "Identifiants invalides ou accès refusé.")
            return redirect('index')
    else:
        messages.warning(request, "Vous devez vous connecter en tant que superuser.")
        return redirect('index')
    

def modifier_produit(request, id):
    produit = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('accueil')
    else:
        form = ProductForm(instance=produit)
    return render(request, 'shop/modifier_produit.html', {'form': form})
