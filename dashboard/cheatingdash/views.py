from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from cheatingdash.models import PaytmHistory,StatusHistory,UserProfile,userSubscriptions
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
import csv
from django.db.models import Sum,Count
from django.http import JsonResponse
from cheatingdash.forms import  userForm
import datetime

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
def Deleteuser(request, id):
    user = UserProfile.objects.get(id = id)
    user.delete()
    return redirect('/userList')


def Detailsuser(request, id):
    user = UserProfile.objects.get(id = id)
    return render(request, 'detailsuser.html', {'user': user})
    

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
        print(data)
        user  = UserProfile.objects.filter(create_at__icontains= data)  

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
def verify_phone(phone):
    if len(phone)==10:
        return (True,'valid')
    elif '+' in phone:
        return (False,'invalid')
    else:
        return None

def send_otp(request): 
    if request.method=="POST":
        data = request.POST.dict()
        data = json.loads(request.body)
        phone = data['phone']
        print(phone)
        if verify_phone(data['phone'])[0]:
            pass
        else:
            return JsonResponse({'status':False,'msg':'invalid number'})
        msg91key = '263002Ai7e8CMeu55c6662f1'
        digits="0123456789"
        otp = ""
        for i in range(6) : 
            otp += digits[math.floor(random.random() * 10)] 
        otp_msg = 'http://control.msg91.com/api/sendotp.php?authkey={0}&message=%3C%23%3E%20{1} is the OTP for Cheatingnot admin login%3A%20%20{2}&sender=CHTNOT&mobile=91{3}&otp={4}'.format(msg91key,otp,phone,otp)
        headers = {"content-type": "application/json"}
        resp = requests.get(otp_msg,headers=headers)
        print(resp.json())
        return HttpResponse('OTP send')
    else:
        return JsonResponse({'status':False,'msg':'invalid request'})

def userUpdate(request, id):
    obj = UserProfile.objects.get(pk = id)    
    form = userForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/userlist')

        
    return render(request, 'userupdate.html', {'form': obj})

def userAnalytics(request):
    labelpro = []
    datapro = []
    labels = []
    data = []
    labelss = []
    datas = []
    user = User.objects.all()
    totalusers=User.objects.all().count()
    userSubscription=userSubscriptions.objects.values('user').annotate(price=Sum('price'))
    UserProfiles = UserProfile.objects.filter(create_at__lte=datetime.datetime.today(), create_at__gt=datetime.datetime.today()-datetime.timedelta(days=30)).\
    values('create_at').annotate(count=Count('id'))
    for usersdatapro in UserProfiles:
        labelpro.append(usersdatapro['create_at'])
        datapro.append(usersdatapro['count'])
        prosdata={
            "plabels":labelpro,
            "pdata":datapro
        }
        print(prosdata)
    print(UserProfiles)
    userSubscription=userSubscriptions.objects.values('user').annotate(price=Sum('price'))

    for usersdata in userSubscription:
        labelss.append(usersdata['user'])
        datas.append(usersdata['price'])
        usdata={
            "ulabels":labelss,
            "udata":datas
        }
        print(usdata)
    PaytmHistorys=PaytmHistory.objects.values('user').annotate(TXNAMOUNT=Sum('TXNAMOUNT'))
    # print(PaytmHistorys)
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
    return render(request,'useranalytics.html',{'users':user,'totalusers':totalusers,'userSubscriptions':userSubscription,'adata':data,'usdata':usdata})

    





