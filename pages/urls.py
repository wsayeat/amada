from django.urls import path
from . import views

"""
{% url 'main:home' %}
{% url 'users:home' %}
"""
app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("shop/", views.shop_view, name="shop"),
    path("shop/categories/<slug:slug>/", views.category_products, name="category_products")
]
