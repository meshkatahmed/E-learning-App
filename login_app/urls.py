from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('register/',views.register,name='register'),
]
