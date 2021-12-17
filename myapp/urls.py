from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product', views.product_list, name="products"),
    path("product/<int:id>", views.product_show, name="product_show"),
    path('product/create', views.product_create, name="product_create"),
    path('product/<int:id>/edit', views.product_edit, name="product_edit"),
    path('product/<int:id>/delete', views.product_destroy, name="product_destroy"),
]
