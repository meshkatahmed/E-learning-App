from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from . import models
from django.urls import reverse,reverse_lazy
from django.views.generic import View,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.
def home(request):
    return HttpResponse('Welcome to homepage')
class WriteArticle(LoginRequiredMixin,CreateView):
    model = models.Article
    fields = ['title','content','image']
    template_name = 'learning_app/writearticle.html'

    def form_valid(self,form):
        article_obj = form.save(commit=False)
        article_obj.author = self.request.user
        article_obj.slug = article_obj.title.replace(" ","-") + "-" + str(uuid.uuid4())
        article_obj.save()
        return HttpResponseRedirect(reverse('home'))
