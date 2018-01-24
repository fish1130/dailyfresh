from django.shortcuts import render, redirect
from df_user.models import Passport

# Create your views here.

def register(request):
    return render(request, 'df_user/register.html')

def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    Passport.objects.add_one_passport(username=username, password=password, email=email)

    return redirect('/user/login/')


