from django.urls import path
from . import views

app_name = 'login_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.registration_form,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
]
