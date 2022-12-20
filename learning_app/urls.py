from django.urls import path
from . import views

app_name = 'learning_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('addarticle/',views.AddArticle.as_view(),name='addarticle'),
]
