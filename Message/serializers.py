from rest_framework import serializers
from .models import Message
from appuser.models import AppUser


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message']

class AppUserSerializer(serializers.ModelSerializer):
    messages = serializers.StringRelatedField(many=True)

    class Meta:
        model = AppUser
        fields = ['bio','location']
