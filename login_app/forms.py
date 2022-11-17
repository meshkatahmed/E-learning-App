from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms

class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
class UserProfileForm(forms.ModelForm):
    is_teacher = forms.BooleanField(required=False)
    is_student = forms.BooleanField(required=False)
    class Meta:
        model = UserProfile
        fields = ['is_teacher','is_student']
