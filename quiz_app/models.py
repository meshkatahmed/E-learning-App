from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
    asking = models.CharField(max_length=265)
    marks = models.IntegerField(default=5)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.asking

class Answer(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question')
    statement = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.statement
