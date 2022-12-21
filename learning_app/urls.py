from django.urls import path
from . import views

app_name = 'learning_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('writearticle/',views.WriteArticle.as_view(),name='writearticle'),
    path('arrangequiz/',views.ArrangeQuiz.as_view(),name='arrangequiz'),
]
