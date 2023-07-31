from django.shortcuts import render
from .forms import ImageForm
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    return render(request,'core/index.html',{
        'form':form
    })
