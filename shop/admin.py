from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','date_added')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_added')
    search_fields = ('title', 'description')
    list_filter = ('category', 'date_added')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
