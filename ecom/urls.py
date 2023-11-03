from django.urls import path
from ecom.views import *


urlpatterns = [
    path("", home, name="home"),
]
