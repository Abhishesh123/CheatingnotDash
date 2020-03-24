from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def Index(request):
    user = User.objects.all()
    print(user)
    return HttpResponse('Thanks')

def userList(request):
    user = User.objects.all()
    print(user)
    return render(request, 'userlist.html', {'users':user})


def Login(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username = username, password=  password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('userList')
        else:
            return HttpResponse("Invalid login details..")
    else:
        return render(request,'login.html')
    

def Logout(request):
    logout(request)
    return redirect('/')

def Delete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('userList')