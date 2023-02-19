from django import forms
from .models import Question,Answer

#Forms
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        exclude = ['user','answer_to_question']
