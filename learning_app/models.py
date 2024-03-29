from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='article_author')
    title = models.CharField(max_length=264,verbose_name='Put a title')
    slug = models.SlugField(max_length=264,unique=True)
    content = models.TextField(verbose_name='Write your mind')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date',]
    def __str__(self):
        return self.title
