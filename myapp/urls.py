from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('student/<int:roll>/<str:name>', views.product),
    path('product_form', views.student_form, name="student_form"),
    path('product', views.products, name="product"),
    path('productshow', views.product_list, name="productshow"),
    path('productedit/<int:id>', views.productedit, name="productedit"),
    path('productdestory/<int:id>', views.productdestroy, name="productdestroy"),
]
