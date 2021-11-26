from django.shortcuts import render 
from .models import Shop, Product, Deal


# Create your views here.
def index(req):
    shops = Shop.objects.all()
    products = Product.objects.all()
    deals = Deal.objects.all()
    context = {
        "shops" : shops,
        "products" : products,
        "deals" : deals
    }
    return render(req, "myapp/index.html", context)

def product_list(req):
    product = Product.objects.all()
    context = {
        'products': product_list
    }
    return render(req, 'product_list.html', context)