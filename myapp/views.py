from django.shortcuts import render,redirect
from .form import ProductForm
from django.contrib import messages
from .models import ProductModel


# Create your views here.
def ProductAdd(request):
    if request.method == 'POST':
        form =ProductForm(request.POST)
        show = ProductModel.objects.all()
        if form.is_valid():
            form.save()
            messages.success(request,'Added Successfully')
            return redirect('/')
    else:
        form =ProductForm()
        show = ProductModel.objects.all()
    context = {'form':form,'show':show}
    return render(request, 'home.html',context)

def Productdelete(request,id):
    data = ProductModel.objects.get(id=id)
    data.delete()
    messages.error(request, 'Deleted')
    return redirect('/')