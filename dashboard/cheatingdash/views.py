from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from cheatingdash.forms import ContactForm, userForm, empForm
from cheatingdash.models import Employee
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filter import employeeFilter

# Create your views here.
def Index(request):
    return HttpResponse('Thanks')

def userList(request):
    user = User.objects.filter(is_active = True)
    column_list = ['Active','Age','City','Country','Gender']
    print(user.count())
    context =  {
        'users':user,
        'Total':user.count(),
        'columns':column_list
        }
    return render(request, 'userlist.html',context)


def Block(request, id):
    user = User.objects.get(pk = id)
    user.is_active = False
    user.save()
    return redirect('/userlist')

def unBlock(request, id):
    user = User.objects.get(pk = id)
    user.is_active = True
    user.save()
    return redirect('/userlist')

def blockUsers(request):
    user = User.objects.filter(is_active = False)
    return render(request, 'block-user.html', {'users':user})
    
    
    
def empList(request):
    emp = Employee.objects.all()
    emp_filter = employeeFilter(request.GET, queryset = emp)
    page = request.GET.get('page', 1)
    paginator = Paginator(emp, 2)
    try:
        emps = paginator.page(page)

    except PageNotAnInteger:
        emps = paginator.page(1)
    except EmptyPage:
        emps = paginator.page(page.num_pages)
    context =  {
        'emps':emps,
        'emp':emp_filter
    }
    return render(request, 'emplist.html',context)

def create(request):
    if request.method == 'POST':
        name = request.POST['empname']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        emp = Employee(name = name, email = email, city = city, state = state)
        emp.save()
        return redirect('/emp')

    return render(request, 'create_emp.html')


def empupdate(request, id):
    obj = get_object_or_404(Employee, pk = id)
    print(obj)
    form = empForm(request.POST or None, instance = obj)
    print(form)
    # if request.method == 'POST':
    #     obj.name = request.POST['empname']
    #     obj.email = request.POST['email']
    #     obj.city = request.POST['city']
    #     obj.state = request.POST['state']
    #     obj.save()
       
    #     return redirect('/emp')

    if form.is_valid():
        form.save()
        return redirect('/emp')
    
    return render(request, 'emp_update.html', {'emp': form})


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


def Edit(request, id):
    obj = User.objects.get(pk = id)    
    return render(request, 'userupdate.html', {'form': obj})


def Update(request, id):
    obj = User.objects.get(pk = id)    
    form = userForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/userlist')

        
    return render(request, 'userupdate.html', {'form': obj})

def searchUser(request):
    if request.method == 'POST':
        data = request.POST['searchnow']
        date_joined = request.POST['datejoined']
        date_joined1 = request.POST['datejoined1']
        print(date_joined1)
        
       
        # user  = User.objects.filter(first_name__icontains= data) or User.objects.filter(date_joined__icontains= date_joined) or User.objects.filter(last_name__icontains= data) or User.objects.filter(username__icontains= data) or User.objects.filter(email__icontains= data) or User.objects.filter(date_joined__icontains= date_joined)
        
        user = User.objects.filter(date_joined__range = (date_joined, date_joined1))
        print(user)

        context =  {
            'users':user,
            'Total':user.count()
           
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



# import json

# import requests
def sendSMS(request):
    if request.method == 'POST':
        number = request.POST['phone']
        senderid = request.POST['senderid']
        msgs = request.POST['msg']
        print(number)
        print(senderid)
        print(msgs)
        # URL = 'https://www.sms4india.com/api/v1/sendCampaign'

        # # get request
        # def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        #     req_params = {
        #         'apikey':apiKey,
        #         'secret':secretKey,
        #         'usetype':useType,
        #         'phone': phoneNo,
        #         'message':textMessage,
        #         'senderid':senderId
        #         }
        #     return requests.post(reqUrl, req_params)

        # # get response
        # response = sendPostRequest(URL, 'api_key', 'secretKey', 'stage', number, senderid, msgs )
        # """
        # Note:-
        #     you must provide apikey, secretkey, usetype, mobile, senderid and message values
        #     and then requst to api
        # """
        # # print response if you want
        # print(response.text)
    return render(request, 'send-sms.html')