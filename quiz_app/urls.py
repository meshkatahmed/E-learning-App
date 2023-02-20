from django.urls import path
from . import views

app_name = 'quiz_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('getquiz/',views.get_quiz,name='getquiz'),
    path('evaluatequiz/',views.evaluate_quiz,name='evaluatequiz'),
]
