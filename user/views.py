from django.shortcuts import render, redirect
from .forms import Signupform
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Signupform()
    return render(request, 'user/signup.html', {'form':form})

@login_required
def logout_views(request):
    logout(request)
    return redirect('home')