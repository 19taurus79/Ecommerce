"""This module contains the views"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from .models import Product, Category

# Create your views here.


def home(request):
    """Представление домашней страницы"""
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)
    return render(
        request,
        "ecom/home.html",
        {"products": products, "categories": categories},
    )


def about(request):
    """Представление страницы "О нас" """
    return render(request, "ecom/about.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Вы вошли в учетную запись"))
            return redirect("home")
        else:
            messages.success(
                request,
                ("Произошла ошибка. Проверьте вводимые данные и попробуйте еще раз."),
            )
            return redirect("login")
    else:
        return render(request, "ecom/login.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, ("Вы вышли из учетной записи"))
    return redirect("home")


def register_user(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Вы успешно зарегестрировались"))
            return redirect("home")
        else:
            messages.success(
                request,
                (
                    "Произошла ошибка. Проверьте правильность вводимых данных и повторите."
                ),
            )
            return redirect("register")
    else:
        return render(request, "ecom/register.html", {"form": form})


def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "ecom/product.html", {"product": product})


def category(request, pk):
    categories = Category.objects.filter(is_active=True)
    cat = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=pk)
    return render(
        request,
        "ecom/category.html",
        {"cat": cat, "products": products, "categories": categories},
    )


def backward(request):
    return_path = request.META.get("HTTP_REFERER", "/")
    return redirect(return_path)
