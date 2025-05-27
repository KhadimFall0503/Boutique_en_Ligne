from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produit/<int:id>/', views.detail_produits, name='detail_produits'),
    path('produits/categorie/<int:categorie_id>/', views.produits_par_categorie, name='produits_par_categorie'),
    path('search/', views.search_results, name='search_results'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Ajout produit par utilisateur connecté
    path('produits/ajouter-mon-produit/', views.ajouter_produit_utilisateur, name='ajouter_produit_utilisateur'),

    # Ajout produit (superuser)
    path('produits/ajouter/', views.ajouter_produit, name='ajouter_produit'),

    # Connexion superuser
    path('superuser-login/', views.superuser_login, name='superuser_login'),

    # Déconnexion
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
