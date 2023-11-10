"""This module registers models to be displayed in the administrator panel"""
from django.contrib import admin
from .models import Order, Product, Category, Customer
from import_export.admin import ImportExportModelAdmin


class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    """This class describes the display of the model in the admin panel"""

    list_display = [
        "name",
        "description",
        "price",
        "category",
        "is_active",
        "is_reserved",
    ]
    list_filter = [
        "category",
        "is_active",
        "is_reserved",
    ]
    list_editable = ["is_active", "is_reserved"]

    search_fields = ["name"]


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["is_active"]


admin.site.register(Category, CategoryAdmin)

# Register your models here.
admin.site.register(Order)


admin.site.register(Customer)
