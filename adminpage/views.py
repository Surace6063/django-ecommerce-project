from django.shortcuts import redirect, render
from product.forms import CategoryForm,ProductForm
from product.models import Product

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_category')

    else:
        form = CategoryForm()        

    return render(request,'add_category.html',{'form':form})


# add product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')

    else:
        form = ProductForm()        

    return render(request,'add_product.html',{'form':form})


# getting products
def products(request):
    product_lists = Product.objects.all()
    return render(request,'dashboard_product_lists.html',{'products':product_lists})