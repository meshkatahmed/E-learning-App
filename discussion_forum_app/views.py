from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView
from .models import Question,Answer
from .forms import QuestionForm,AnswerForm
from django.contrib import messages

# Create your views here.
class Questions(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'discussion_forum_app/discussionhome.html'

@login_required
def question_detail(request,pk):
    questions = Question.objects.filter(id=pk)
    answers = Answer.objects.filter(answer_to_question=questions[0])
    diction = {'question':questions[0],'answers':answers}
    return render(request,'discussion_forum_app/answeraquestion.html',context=diction)

@login_required
def ask_question(request):
    if not request.user.user_profile.is_teacher:
        form = QuestionForm

        if request.method=='POST':
            form = QuestionForm(request.POST)
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('discussion_forum_app:discussionhome')
    else:
        messages.warning(request,'A teacher account cannot ask question!!')
        return redirect('discussion_forum_app:discussionhome')

    diction = {'form':form}
    return render(request,'discussion_forum_app/askquestion.html',context=diction)

@login_required
def answer_question(request,pk):
    questions = Question.objects.filter(id=pk)
    answers = Answer.objects.filter(answer_to_question=questions[0])
    if request.user.user_profile.is_teacher:
        form = AnswerForm

        if request.method=='POST':
            form = AnswerForm(request.POST)
            form = form.save(commit=False)
            form.user = request.user
            form.answer_to_question = questions[0]
            form.save()
            return redirect('discussion_forum_app:answeraquestion', pk=questions[0].pk)

    else:
        messages.warning(request,'A non-teacher account cannot answer a question')
        return redirect('discussion_forum_app:answeraquestion', pk=questions[0].pk)

    diction = {'form':form,'question':questions[0],'answers':answers,'to_answer':True}
    return render(request,'discussion_forum_app/answeraquestion.html',context=diction)
