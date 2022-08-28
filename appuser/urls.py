from django.urls import path,include
from .views import CreateUserView,test_page,test_failure,EditAppUser

app_name='userapp'

urlpatterns = [
    path('register/',CreateUserView.as_view(),name='register'),
    path('register/<int:userid>',EditAppUser.as_view(),name='appuser_update'),
    path('success/', test_page, name='success_page'),
    path('failure/', test_failure, name='failure_page'),
]