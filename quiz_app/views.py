from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from .models import *
import random
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required
def home(request):
    if not request.user.user_profile.is_teacher:
        messages.info(request,'A non-teacher account cannot make a quiz')
        return redirect('login_app:home')
    diction = {'categories':Category.objects.all()}
    return render(request,'quiz_app/arrangequiz.html',context=diction)

def get_quiz(request):
    if request.method=='GET':
        categories = Category.objects.filter(name=request.GET['category'])
        questions = Question.objects.filter(category=categories[0])
        questions = list(questions)
        data = []
        random.shuffle(questions)
        for question in questions:
            data.append({'question':question.asking,'answers':question.get_answers(),'marks':question.marks})
            print(data)
            diction = {'data':data}
        return render(request,'quiz_app/getquiz.html',context=diction)
    else:
        messages.info(request,'Please select a category')
        return redirect('quiz_app:home')
