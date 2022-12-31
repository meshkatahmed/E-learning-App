from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserForm,UserProfileForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.
def home(request):
    diction = {'message':'Welcome to login_app homepage'}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        userinfo = User.objects.get(pk=user_id)
        userprofileinfo = UserProfile.objects.get(user__pk=user_id)
        diction.update({'userinfo':userinfo,'userprofileinfo':userprofileinfo})
    return render(request,'login_app/home.html',context=diction)
def registration_form(request):
    registered = False
    if request.method=='POST':
        userform = UserForm(request.POST)
        userprofileform = UserProfileForm(request.POST,request.FILES)
        if userform.is_valid() and userprofileform.is_valid():
            user = userform.save()
            userprofile = userprofileform.save(commit=False)
            userprofile.user = user
            if 'profile_pic' in request.FILES:
                userprofile.profile_pic = request.FILES['profile_pic']
            userprofile.save()
            registered = True
    else:
        userform = UserForm()
        userprofileform = UserProfileForm()
    diction = {'userform':userform,'userprofileform':userprofileform,'registered':registered}
    return render(request,'login_app/registrationform.html',context=diction)
def user_login(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return HttpResponseRedirect(reverse('login_app:home'))
    return render(request,'login_app/loginform.html',context={'form':form})
@login_required
def user_logout(request):
    logout(request)
    return render(request,'login_app/logoutform.html',context={})
