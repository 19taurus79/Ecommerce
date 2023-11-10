"""This module describes the database models"""
import datetime
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.


class Category(models.Model):
    """A category model"""

    name = models.CharField(max_length=50, verbose_name="Категория")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("category", args=[int(self.pk)])

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Customer(models.Model):
    """A customer model"""

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=15, verbose_name="Телефон")
    email = models.EmailField(max_length=100, verbose_name="Электронная почта")
    password = models.CharField(max_length=100, verbose_name="Пароль")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Product(models.Model):
    """A product model"""

    name = models.CharField(max_length=100, verbose_name="Наименования")
    price = models.DecimalField(
        max_digits=6, default=0, decimal_places=2, verbose_name="Цена"
    )
    category = models.ForeignKey(
        Category, default=1, on_delete=models.CASCADE, verbose_name="Категория"
    )
    description = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Описание"
    )
    image = models.ImageField(upload_to="uploads/products", verbose_name="Фотография")
    is_sale = models.BooleanField(default=False, verbose_name="Распродажа")
    sale_price = models.DecimalField(
        max_digits=6, default=0, decimal_places=2, verbose_name="Цена распродажи"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_reserved = models.BooleanField(default=False, verbose_name="Резерв")
    payment = models.BooleanField(default=False, verbose_name="Оплачен")
    created = models.DateTimeField(default=timezone.now(), verbose_name="Добавлен")

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("product", args=[(int(self.pk))])

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):
    """An order model"""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name="Покупатель"
    )
    quantity = models.IntegerField(default=1, verbose_name="Количество")
    address = models.CharField(
        max_length=100, default="", blank=True, verbose_name="Адрес"
    )
    phone = models.CharField(
        max_length=15, default="", blank=True, verbose_name="Телефон"
    )
    date = models.DateField(default=timezone.now(), verbose_name="Дата покупки")
    status = models.BooleanField(default=False, verbose_name="Статус")

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
