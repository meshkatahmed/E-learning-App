from django.urls import path
from . import views
app_name = 'discussion_forum_app'

urlpatterns = [
    path('',views.Questions.as_view(),name='discussionhome'),
    path('askquestion/',views.ask_question,name='askquestion'),
    path('answeraquestion/<pk>/',views.question_detail,name='answeraquestion'),
    path('answerquestion/<pk>/',views.answer_question,name='answerquestion'),
]
