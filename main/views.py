from django.shortcuts import render
from .models import Post

def home(request):
    context = {'posts':Post.objects.all()}
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html', {'title':'About'})