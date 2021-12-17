from django.http import request
from django.http.response import HttpResponseForbidden
from django.shortcuts import redirect, render 
from .models import Shop, Product, Deal
from django.contrib import messages
from .forms import ProductForm

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
        'products': product
    }
    return render(req, 'myapp/product/list.html', context)

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Created sucessfully")
            return redirect("/product/create")
        else:
            messages.error(request, "Cannot store data")
            return redirect("/product/create")
    form = ProductForm()
    return render(request, "myapp/product/create.html",{
        "form" : form
    } )
 
def product_show(req, id):
    product = Product.objects.get(id=id)
    return render(req, "myapp/product/show.html", {"product": product})

def product_edit(req, id):
    if req.method == "POST":
        form = ProductForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Created sucessfully")
            return redirect("/product/edit/" + str(id))

        else:
            messages.error(request, "Cannot store data")
            return redirect("/product/edit/" + str(id))

    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    return render(req, "myapp/product/edit.html", {"form" : form})

def product_destroy(req, id):
    if req.method == "POST":
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('/product')
    return HttpResponseForbidden("GET Request NOT ALLOWED")
