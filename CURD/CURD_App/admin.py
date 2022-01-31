from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'model_name', 'price', 'color', 'date']

admin.site.register(Product, ProductAdmin)