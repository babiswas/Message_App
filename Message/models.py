from django.db import models
from django.contrib.auth.models import User
from appuser.models import AppUser

# Create your models here.

def get_default_user():

    '''Default user is admin'''

    return User.objects.get(pk=1)

def get_default_user_id():

    '''Default user id'''

    return get_default_user().id


class Message(models.Model):

    '''Message for the users'''

    message=models.TextField(max_length=500)
    receiver=models.ForeignKey(AppUser,on_delete=models.SET(get_default_user),default=get_default_user_id,related_name='messages')
    sender=models.ForeignKey(User,on_delete=models.DO_NOTHING)


    def __init__(self):
        return self.message


