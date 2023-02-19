from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from django.contrib import messages

# Create your views here.
class Articles(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'learning_app/learninghome.html'

class ArticleDetail(LoginRequiredMixin,DetailView):
        model = Article
        context_object_name = 'article'
        template_name = 'learning_app/articledetail.html'

@login_required
def write_article(request):
    if request.user.user_profile.is_teacher:
        form = ArticleForm

        if request.method=='POST':
            form = ArticleForm(request.POST)
            form_saved = form.save(commit=False)
            form_saved.author = request.user
            form_saved.slug = form_saved.title.replace(" ","-")+"-"+str(uuid.uuid4())
            form_saved.save()
            return redirect('learning_app:articles')
        diction = {'form':form}
        return render(request,'learning_app/writearticle.html',context=diction)
    else:
        messages.info(request,'A non-techer account cannot write article')
        return redirect('learning_app:articles')
