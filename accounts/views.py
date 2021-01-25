from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import *


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #user = form.get_user()
            #login(request, user)
                #loguser in
            return redirect ('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #Loguser in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('portal')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('logoutlanding')

@login_required(login_url="/accounts/login/") #This view nees to be fixed, it's logging the user out
def profile_view(request):
    if request.method == 'POST':
        form = forms.ProfileForm(request.POST) #Use if no images on form
        if form.is_valid():
            form.save()
    else:
        form = ProfileForm()
        return render(request, 'accounts/profile.html', {'form':form})
