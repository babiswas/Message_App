from rest_framework import serializers
from .models import Message
from appuser.models import AppUser


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message','sender']

class AppUserSerializer(serializers.ModelSerializer):
    messages =MessageSerializer(many=True,read_only=True)

    class Meta:
        model = AppUser
        fields = ['bio','location','messages']
