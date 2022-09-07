from rest_framework import serializers
from .models import Message
from appuser.models import AppUser
from appuser.serializers import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message','sender']

class AppUserSerializer(serializers.ModelSerializer):

    '''Appuser Serializer'''

    messages =MessageSerializer(many=True,read_only=True)
    created_by=UserSerializer(read_only=True)

    class Meta:
        model = AppUser
        fields = ['bio','location','messages','created_by']
