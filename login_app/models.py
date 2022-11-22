from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user_profile')
    profile_pic = models.ImageField(upload_to='static/images/profilepics',default='static/images/x.jpg')
    status_choices = (('Teacher','Teacher'),('Student','Student'))
    status = models.CharField(max_length=264,choices=status_choices)

    def __str__(self):
        return self.user.username + ' ' + self.status
