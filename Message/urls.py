from django.urls import path,include
from .views import message_list,MessageAPI,appuser_list

app_name='Message'

urlpatterns = [
    path('messages/',message_list,name='messages'),
    path('read_write_message/',MessageAPI.as_view(),name='rwmessage'),
    path('appuserlist/',appuser_list,name='app_user_list'),
]