from django.http import request
from django.shortcuts import redirect, render 
from .models import Shop, Product, Deal, Student
from django.contrib import messages
from myapp.forms import ProductForm


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
    return render(req, 'myapp/product_list.html', context)

def product(req, roll, name):
    print(roll)
    print(name)
    context = {"roll" : roll, "name" : name}
    return render(req, "myapp/product.html", context)

def student_form(req):
    if req.method == "POST":
        username = req.POST["username"]
        roll = req.POST["roll"]
        student = Student.objects.create(username=username, roll=roll)
        student.save()
        messages.success(req, "Student created sucessfully !")
        return redirect('student_form');
        
    return render(req, "myapp/form.html")

def products(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Created sucessfully")
            return redirect('/product')
        else:
            messages.error(request, "Cannot store data")
            return redirect("/product")
    form = ProductForm()
    return render(request, "myapp/product_new.html",{
        "form" : form
    } )
 

def productedit(req, id):
    if req.method == "POST":
        form = ProductForm(req.POST, req.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Created sucessfully")
            return redirect('/productedit')
        else:
            messages.error(request, "Cannot store data")
            return redirect("/productedit")
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    return render(req, "myapp/product_edit.html", {"form" : form})

def productdestroy(req, id):
   if request.method == "POST":
       product = Product.objects.get(id=id)
       product.delete()
    
   return redirect('/productshow') 