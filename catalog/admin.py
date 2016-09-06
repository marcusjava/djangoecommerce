from django.contrib import admin
from .models import Product,Category


class CategoryAdmin(admin.ModelAdmin):
    """class de customização do admin"""
    list_display = ['name','created','updated_at']
    search_fields = ['name']
    list_filter = ['created','updated_at']

class ProductAdmin(admin.ModelAdmin):
    """customização do produto admin"""
    list_display = ['name','description','category','price','created','updated_at']
    search_fields = ['name','category__name']
    list_filter = ['created','updated_at']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
