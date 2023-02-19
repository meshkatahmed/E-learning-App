from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Question(BaseModel):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='user_question')
    asking = models.CharField(max_length=264)

class Answer(BaseModel):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='user_answer')
    answer_to_question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='question')
    statement = models.TextField()
