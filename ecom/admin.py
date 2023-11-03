"""This module registers models to be displayed in the administrator panel"""
from django.contrib import admin
from .models import Order, Product, Category, Customer


class ProductAdmin(admin.ModelAdmin):
    """This class describes the display of the model in the admin panel"""

    list_display = [
        "name",
        "description",
        "price",
        "category",
    ]
    list_filter = [
        "name",
        "category",
    ]


# Register your models here.
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer)
