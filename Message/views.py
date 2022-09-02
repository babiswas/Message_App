from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Message
from appuser.models import AppUser
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from .serializers import MessageSerializer,AppUserSerializer
from rest_framework.decorators import renderer_classes
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def message_list(request):

    '''Message list controller using JSONRenderer'''

    messages=Message.objects.all()
    all_message=MessageSerializer(messages,many=True)
    return Response(all_message.data)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def appuser_list(request):

    '''Appuser list controller using JSONRenderer'''

    appuser=AppUser.objects.all()
    all_app_user=AppUserSerializer(appuser,many=True)
    return Response(all_app_user.data)


class MessageAPI(APIView):

    '''Message related apis'''

    def get(self,request):

        '''Method to read all the messages.'''

        messages=Message.objects.all()
        all_message=MessageSerializer(messages,many=True)
        return Response(all_message.data)

    def post(self,request,format=None):

        '''Method to create a message'''

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)












