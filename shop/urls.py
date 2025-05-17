from django.contrib import admin
from django.urls import path
from .views import index,liste_produits,detail_produits

urlpatterns = [
    path('', index, name='index' ),
    path('produits/', liste_produits, name='liste_produits' ),
    path('detail/<int:id>/', detail_produits, name='detail_produits'),


]
