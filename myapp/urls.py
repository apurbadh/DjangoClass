from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product_list', views.product_list, name="product_list"),
    path('student/<int:roll>/<str:name>', views.product),
    path('product_form', views.form)
]
