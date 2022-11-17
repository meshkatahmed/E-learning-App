from django.shortcuts import render
from .forms import UserForm,UserProfileForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def home(request):
    return HttpResponse('Welcome to the account creation page')
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login_app:home'))
    return render(request,'loginapp/registrationform.html',context={'form':form})
