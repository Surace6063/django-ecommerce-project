from django.http import HttpResponse
from django.shortcuts import render
from . models import Product

# Create your views here.
def products(request):
    product_lists = Product.objects.all().order_by('-id')
    items = {
        "products":product_lists
        }

    return render(request,'product/product_lists.html',items)


def product_details(request,product_id):
    product = Product.objects.get(id = product_id)

    data = {
        'product':product
    }
    return render(request,'product/product_details.html',data)