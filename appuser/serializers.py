from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):

    '''User Serializer to display user'''

    id=serializers.IntegerField(read_only=True)
    username=serializers.CharField(required=True, allow_blank=False, max_length=100)
    email=serializers.EmailField(required=True, allow_blank=False)
