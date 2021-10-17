from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm

def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'New account created for {username}')
            return redirect('home') 
    else:
        form = UserRegisterForm(request.POST)

    return render(request, 'users/register.html',{'form': form ,'title':'Register'})

def login(request):
    return render(request, 'users/login.html',{'title':'Login'})