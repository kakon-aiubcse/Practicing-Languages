from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

def home(request):
    return HttpResponse("hello world from blog app with django")

def data(request):
    datas = Post.objects.all()
    return render(request, 'blog/home.html', {'datas' : datas})
