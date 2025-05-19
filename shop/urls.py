from django.contrib import admin
from django.urls import path
from .views import index,liste_produits,detail_produits,login_views,search_results,cart_detail,add_to_cart,cart_view,remove_from_cart

urlpatterns = [
    path('', index, name='index' ),
    path('produits/', liste_produits, name='liste_produits' ),
    path('detail/<int:id>/', detail_produits, name='detail_produits'),
   path('ajouter/<int:product_id>/', add_to_cart, name='add_to_cart'),
   path('cart/', cart_view, name='cart_view'),
   path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('search/', search_results, name='search_results'),
     path('panier/', cart_detail, name='cart_detail'),



]
