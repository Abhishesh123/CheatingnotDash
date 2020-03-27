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
    print(user.count())
    return render(request, 'userlist.html', {'users':user,'Total':user.count()})
    


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


def Details(request, id):
    user = User.objects.get(id = id)
    return render(request, 'details.html', {'user': user})


def searchUser(request):
    if request.method == 'POST':
        data = request.POST['searchnow']
        data = request.POST['datejoined']
        print(data)
        user  = User.objects.filter(first_name__icontains= data) or User.objects.filter(last_name__icontains= data) or User.objects.filter(username__icontains= data) or User.objects.filter(email__icontains= data) or User.objects.filter(date_joined__icontains= data)

        return render(request, 'userlist.html', {'users':user, 'Total':user.count()})