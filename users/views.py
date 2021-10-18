from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'New account created for {username}! You can login now!')
            return redirect('login') 
    else:
        form = UserRegisterForm(request.POST)

    return render(request, 'users/register.html',{'form': form ,'title':'Register'})

@login_required
def profile(request):
    return render(request, 'users/profile.html',{'title':'profile'})