from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from cheatingdash.models import PaytmHistory,StatusHistory,UserProfile,userSubscriptions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
import csv
from django.db.models import Sum
from django.http import JsonResponse

# Create your views here.
@login_required(login_url='/login/')
def Index(request):
    labels = []
    data = []
    user = User.objects.all()
    totalusers=User.objects.all().count()
    userSubscription=userSubscriptions.objects.all().count()
    PaytmHistorys=PaytmHistory.objects.values('user').annotate(TXNAMOUNT=Sum('TXNAMOUNT'))
    print(PaytmHistorys)
    # labels= ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    # chartLabel =userSubscriptionss
    for entry in PaytmHistorys:
        labels.append(entry['user'])
        data.append(entry['TXNAMOUNT'])
    # chartdata = [0, 10, 5, 2, 20, 30, 45]
    data={
                     "labels":labels,
                     # "chartLabel":chartLabel,
                     "chartdata":data,
             }
    return render(request,'homepage.html',{'users':user,'totalusers':totalusers,'userSubscriptions':userSubscription,'data':data})


def Login(request):
    if request.method == 'POST':
        username  = request.POST.get('username')
        password  = request.POST.get('password')
        user = authenticate(username = username, password=  password)
        if user:
            if user.is_active:
                login(request,user)
                return render(request, 'homepage.html')
        else:
            return HttpResponse("Invalid login details..")
    else:
        return render(request,'login.html')
    

def Logout(request):
    logout(request)
    return redirect('/')

def paymentStatus(request):
    user = PaytmHistory.objects.all()
    print(user)
    # metrics = {
    #         'total': count(id),
    #         'total_sales': Sum(TXNAMOUNT),
    #     }
    return render(request, 'paymentstatus.html', {'users':user})

def StatusHistorys(request):
    users = StatusHistory.objects.all()
    
    return render(request, 'statushistory.html', {'users':users})

def PaydetailStatus(request, id):
    user = StatusHistory.objects.get(id = id)
    return render(request, 'paydetailstatus.html', {'user': user})

def Paymentdetail(request, id):
    user = PaytmHistory.objects.get(id = id)
    return render(request, 'paymentdetails.html', {'user': user})

def userList(request):
    user = UserProfile.objects.all()
    print(user)
    return render(request, 'userlisting.html', {'users':user})


def userListCSV(request):

    # Get all data from UserDetail Databse Table
    users = UserProfile.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="userlist.csv"'

    writer = csv.writer(response)
    writer.writerow(['User ID', 'Username', 'Age ','Phone', 'Address','Created Date'])

    for user in users:
        writer.writerow([user.id, user.user, user.age, user.phone,user.address,user.create_at|date])

    return response

def searchUser(request):
    if request.method == 'POST':
        data = request.POST['q']
        # data = request.POST['datejoined']
        print(data)
        user  = UserProfile.objects.filter(age__icontains= data) or UserProfile.objects.filter(phone__icontains= data) or UserProfile.objects.filter(user__icontains= data) or UserProfile.objects.filter(create_at__icontains= data)

        return render(request, 'userlisting.html', {'users':user})

def datefilter(request):
    if request.method == 'POST':
        data = request.POST['start']
        data1 = request.POST['end']
        print(data)
        user  = UserProfile.objects.filter(create_at__icontains= data)  and UserProfile.objects.filter(create_at__icontains= data)

        return render(request, 'userlisting.html', {'users':user})

def userSubscription(request):
    user = userSubscriptions.objects.all()
    print(user)
    return render(request, 'userSubscriptions.html', {'users':user})

def userSubscriptionDetails(request, id):
    user = userSubscriptions.objects.get(id = id)
    print(user)
    return render(request, 'userSubscriptionDetails.html', {'users':user})



def userSubscriptionsCSV(request):

    # Get all data from UserDetail Databse Table
    users = userSubscriptions.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="userSubscriptionsCSV.csv"'

    writer = csv.writer(response)
    writer.writerow(['Subscriptions ID', 'Username', 'Subscriptions Plan Name', 'Month','Price','Status'])

    for user in users:
        writer.writerow([user.id, user.user, user.SubsplanName, user.durationMonth,user.price])

    return response

def searchSubscriptions(request):
    if request.method == 'POST':
        data = request.POST['search']
    
        user  = userSubscriptions.objects.filter(SubsplanName__icontains= data) 

        return render(request, 'userSubscriptions.html', {'users':user})

def salescharts(srequest,format=None):
        labels= ['January', 'February', 'March', 'April', 'May', 'June', 'July']
        chartLabel =PaytmHistory.objects.all()
        chartdata = [0, 10, 5, 2, 20, 30, 45]
        data={
                     "labels":labels,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
             }
        return JsonResponse(data)
def resetpassword(request):

    return render(request, 'resetpassword.html')

def sendlink(request):
    if request.method == 'POST':
        data = request.POST['email']
    return render(request, 'resetpassword.html')





