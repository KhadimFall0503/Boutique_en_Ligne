from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),
    path('produits/modifier/<int:id>/', views.modifier_produit, name='modifier_produit'),
    path('produits/supprimer/<int:id>/', views.supprimer_produit, name='supprimer_produit'),
    path('produits/<int:id>/', views.detail_produits, name='detail_produits'),
    path('recherche/', views.search_results, name='search_results'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('categorie/<int:categorie_id>/', views.produits_par_categorie, name='produits_par_categorie'),
     path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
      path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),
]
