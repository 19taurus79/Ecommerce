from django.urls import path
from ecom.views import *


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("register/", register_user, name="register"),
    path("product/<int:pk>", product, name="product"),
    path("category/<int:pk>", category, name="category"),
    path("backward/", backward, name="backward"),
]
