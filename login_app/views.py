from .forms import UserForm,UserProfileForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.
def home(request):
    return HttpResponse('Welcome to the account creation page')
def register(request):
    registered = False
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
            #return HttpResponseRedirect(reverse('login_app:home'))
    return render(request,'loginapp/registrationform.html',context={'form':form,'registered':registered})
def user_login(request):
    user = None
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                #return HttpResponseRedirect(reverse('login_app:home'))
    return render(request,'loginapp/loginform.html',context={'form':form,'user':user})
@login_required
def user_logout(request):
    logout(request)
    #return HttpResponseRedirect(reverse('login_app:home'))
    return render(request,'loginapp/logoutform.html',context={})
