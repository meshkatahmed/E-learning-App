from django.urls import path
from . import views

app_name = 'learning_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('writearticle/',views.write_article,name='writearticle'),
]
