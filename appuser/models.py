from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class AppUser(models.Model):

    '''Model for app user'''

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    location=models.TextField(max_length=30,blank=True)
    registered_date=models.DateTimeField(auto_now_add=True,blank=False)

@receiver(post_save,sender=User)
def create_user_appuser(sender,instance,created,**kwargs):
    if created:
        AppUser.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_user_appuser(sender,instance,created,**kwargs):
    instance.appuser.save()




