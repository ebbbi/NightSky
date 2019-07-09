from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import auth
from django.contrib.auth.models import User
# Create your views here.
def register(request):
    if request.method=="POST":
        if request.POST['password1']!=request.POST['password2']:
            return render(request, 'register_done.html', {'message': '비밀빈호가 일치하지 않습니다'})
        try:
            username=request.POST['username']
            email=request.POST['email']
            password=request.POST['password1']
            new_user=User.objects.create_user(username, email, password)
            new_user.save()
            return render(request, 'register_done.html', {'message': '회원가입이 완료되었습니다'})
        except:
            return render(request, 'register_done.html', {'message': '회원이 이미 있습니다'})
    else:
        form=UserRegisterForm()
        return render(request, 'register.html', {'form':form})

def register_done(request):
    return render(request, 'register_done.html')

def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
