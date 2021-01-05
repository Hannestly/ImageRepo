from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ImageForm
from .classify import classify
from django.core.files.storage import FileSystemStorage
from .filters import DetailFilter, CombinedFilter

# Create your views here.
def home(request):
    images = Image.objects.all()
    if request.method == 'POST':
        upload_file = request.FILES['searchImg']
        image_fs = FileSystemStorage(location='static/images/Upload')
        temp_name = image_fs.save(upload_file.name, upload_file)
        temp_image_path = image_fs.path(temp_name)
        classification = classify(temp_image_path)
        get = request.GET.copy()
        get['tag_filter'] = classification
        request.GET = get
    detailFilter = DetailFilter(request.GET,queryset=images)
    combinedFilter = CombinedFilter(request.GET,queryset=images)
    
    images = detailFilter.qs
    images = combinedFilter.qs

    context = {
        'images':images,
        'detailFilter':detailFilter,
        'combinedFilter':combinedFilter
    }
    return render(request,'repo/dashboard.html', context= context)

def upload(request):
    form = ImageForm()
    context = {'form': form}
    if request.method == 'POST':
        upload_file = request.FILES['temp_image_upload']
        image_fs = FileSystemStorage(location='static/images/Upload')
        img_name = image_fs.save(upload_file.name, upload_file)
        img_path = image_fs.path(img_name)
        classification = classify(img_path)
        
        post = request.POST.copy()
        post['tag'] = classification
        post['image_path'] = image_fs.path(img_name)
        request.POST = post
    
        form = ImageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request,'repo/upload_form.html',context=context)


def deleteImage(request, pk):
    image = Image.objects.get(id=pk)
    context = {'item':image}
    if request.method == "POST":
        image.delete()
        return redirect('/')
    return render(request,'repo/delete.html',context=context)