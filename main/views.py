from django.shortcuts import render
from .models import Post

def home(request):
    context = {'posts':Post.objects.all()}
    return render(request, 'main/index.html', context=context)

def about(request):
    return render(request, 'main/about.html', {'title':'About'})