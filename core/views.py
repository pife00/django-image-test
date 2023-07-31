from django.shortcuts import render
from .forms import ImageForm
from .models import imageData
# Create your views here.

def index(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageForm()
    items = imageData.objects.all();
    return render(request,'core/index.html',{
        'form':form,
        'items':items
    })
