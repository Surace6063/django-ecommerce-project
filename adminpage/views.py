from django.shortcuts import redirect, render
from product.forms import CategoryForm

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('add_category')

    else:
        pass        

    return render(request,'add_category.html',{'form':form})