from django.contrib import admin
from .models import ProductModel
# Register your models here.


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["desc", "price", "name"][::-1]
