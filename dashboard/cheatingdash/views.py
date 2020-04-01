from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.
def Index(request):
    user = User.objects.all()
    print(user)
    return HttpResponse('Thanks')

def userList(request):
    user = User.objects.all()
    column_list = ['Active','Age','City','Country','Gender']
    print(user.count())
    context =  {
        'users':user,
        'Total':user.count(),
        'columns':column_list
        }
    return render(request, 'userlist.html',context)
    


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
        date_joined = request.POST['datejoined']
        filters = request.POST['filter']
        print(data)
        try:
            age = request.POST['age']
            city = request.POST['city']
            country = request.POST['country']
           
            print(age)
            print(city)
            print(country)
            
            try:
                gender = request.POST['gender']
                print(gender)

            except KeyError:
                pass

        except KeyError:
            pass
        
        
        print(filters)
       
        user  = User.objects.filter(first_name__icontains= data) or User.objects.filter(last_name__icontains= data) or User.objects.filter(username__icontains= data) or User.objects.filter(email__icontains= data) or User.objects.filter(date_joined__icontains= date_joined)

        if filters == 'Active':
            user  = User.objects.filter(is_active = True)

       

        
        column_list = ['Active','Age','City','Country','Gender']
        context =  {
            'users':user,
            'Total':user.count(),
            'columns':column_list
            }
        return render(request, 'userlist.html', context)


def ContactMe(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipientss = []
            recipients  = form.cleaned_data['recipients']
            cc_myself = form.cleaned_data['cc_myself']

            sender = 'vishvajitrao@gmail.com'

            if cc_myself:
                recipientss.append(recipients) 

            send_mail(subject,message,sender,recipientss)
            return HttpResponse('<h1 style=text-align:center;>Thanks for using.. </h1>')
    # if this is a POST  mishra.abhi9619@gmail.com request we need to process the form data

    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})