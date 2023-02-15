from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ArticleForm
from django.urls import reverse,reverse_lazy
from django.views.generic import View,CreateView
from django.contrib.auth.decorators import login_required
import uuid
from django.contrib import messages

# Create your views here.
def home(request):
    diction = {'message':'Welcome to learning_app homepage'}
    return render(request,'learning_app/home.html',context=diction)

@login_required
def write_article(request):
    teaches = request.user.user_profile.is_teacher
    if teaches:
        form = ArticleForm
        diction = {'form':form}
        return render(request,'learning_app/writearticle.html',context=diction)
    else:
        messages.info(request,'A non-techer account cannot write article')
        return redirect('learning_app:home')





#class WriteArticle(LoginRequiredMixin,CreateView):
#    model = models.Article
#    fields = ['title','content','image']
#    template_name = 'learning_app/writearticle.html'
#
#    def form_valid(self,form):
#        article_obj = form.save(commit=False)
#        article_obj.author = self.request.user
#        article_obj.slug = article_obj.title.replace(" ","-") + "-" + str(uuid.uuid4())
#        article_obj.save()
#        return HttpResponseRedirect(reverse('home'))
