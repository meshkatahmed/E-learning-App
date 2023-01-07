from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import random
# Create your views here.

def home(request):
    diction = {'categories':Category.objects.all()}
    return render(request,'quiz_app/arrangequiz.html',context=diction)
    #return HttpResponse('Welcome to quiz_app homepage')

def get_quiz(request):
    question_objs = list(Question.objects.all())
    data = []
    random.shuffle(question_objs)
    for question_obj in question_objs:
        data.append({'category':question_obj.category.name,
        'question':question_obj.asking,'marks':question_obj.marks,
        'answers':question_obj.get_answers()})
    payload = {'status':True,'data':data}
    return JsonResponse(payload)
