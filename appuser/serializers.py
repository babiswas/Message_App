from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AppUser



class UserSerializer(serializers.Serializer):

    '''User Serializer to display user'''

    id=serializers.IntegerField(read_only=True)
    username=serializers.CharField(required=True, allow_blank=False,max_length=100)
    email=serializers.EmailField(required=True, allow_blank=False)


class AppUserSerializer(serializers.Serializer):

    '''A serializer for the app user'''

    id=serializers.IntegerField(read_only=True)
    location=serializers.CharField(required=True, allow_blank=False, max_length=100)
    bio=serializers.CharField(required=True, allow_blank=False, max_length=100)
    user_id=serializers.IntegerField(read_only=True)


class ModelAppUserSerializer(serializers.ModelSerializer):

    ''''ModelAppUserSerializer for app user updation and detail'''
    user=UserSerializer(read_only=True)
    class Meta:
        model = AppUser
        fields = ['bio','location','user']


class ModelUserSerializer(serializers.ModelSerializer):

    ''''ModelAppUserSerializer for app user updation and detail'''

    appuser=ModelAppUserSerializer(read_only=True)

    class Meta:
        model = User
        fields = ["username","email","id","appuser"]


