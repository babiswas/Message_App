from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,AppUserForm
from .models import AppUser
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.utils.six import BytesIO
from rest_framework.decorators import renderer_classes,api_view

# Create your views here.


class CreateUserView(View):

    ''''Create user view to create appuser and user'''

    def get(self,request,*args,**kwargs):

        '''Method to display user form'''

        userform=RegisterForm()
        return render(request,'appuser/register.html',{'userform':userform})


    def post(self,request,*args,**kwargs):

        '''Method to create the user'''

        userform=RegisterForm(request.POST)
        if userform.is_valid() :
            user=userform.save(commit=True)
            print(user)
            return redirect('userapp:appuser_update',userid=user.id)
        else:
            return redirect('userapp:failure_page')

class EditAppUser(View):


    def get(self,request,userid,*args,**kwargs):

        '''Method to display app user form with data populated'''

        appuser=AppUser.objects.filter(user_id=userid)
        appuser_form=AppUserForm(instance=appuser[0])
        return render(request,'appuser/app_user.html',{'appuser_form':appuser_form})


    def post(self,request,userid,*args,**kwargs):

        '''Method to save the app user updated form'''
        appuser = AppUser.objects.filter(user_id=userid)
        appuser_form=AppUserForm(request.POST,instance=appuser[0])
        if appuser_form.is_valid() :
            appuser_form.save()
            return redirect('userapp:success_page')
        else:
            return redirect('userapp:failure_page')


class UserAPI(APIView):

    '''User related apis'''

    def get(self,request):
        users=User.objects.all()
        alluser=UserSerializer(users,many=True)
        return Response(alluser.data)





def test_page(request):

    '''Sucess page method'''

    return render(request,'appuser/success.html')

def test_failure(request):

    '''Failure page method'''

    return render(request,'appuser/failure.html')

@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def user_list(request):
    users=User.objects.all()
    all_user=UserSerializer(users,many=True)
    return Response(all_user.data)







