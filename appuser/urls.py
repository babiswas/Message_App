from django.urls import path,include
from .views import CreateUserView,test_page,test_failure,EditAppUser,UserAPI,user_list,app_user_list,AppUserDetail

app_name='userapp'

urlpatterns = [
    path('register/',CreateUserView.as_view(),name='register'),
    path('register/<int:userid>',EditAppUser.as_view(),name='appuser_update'),
    path('success/', test_page, name='success_page'),
    path('failure/', test_failure, name='failure_page'),
    path('alluser/',UserAPI.as_view(),name='all_user_api'),
    path('accountusers/',user_list,name='test_users'),
    path('app_users/',app_user_list,name='test_users'),
    path('app_user_detail/<int:pk>',AppUserDetail.as_view(),name='app_user_detail'),
]