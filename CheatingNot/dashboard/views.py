from django.shortcuts import render,redirect
import datetime
from django.contrib.sessions.models import Session
from userprofile.models import Users,Match,Reports
from subscription.models import PlanPurchedByUser,PaytmPaymentStatus,PurchaseRequest
from django.utils import timezone
from dashboard.forms import  userForm
from django.db.models import Sum,Count
from django.http import HttpResponse
import csv
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def Index(request):
	today = datetime.date.today()
	todayusers = Users.objects.filter(create_at__date = today).count()
	totaluser = Users.objects.all().count()
	todayMatch = Match.objects.filter(create_at__date = today).count()
	totalMatch = Match.objects.all().count()
	todaysales = PlanPurchedByUser.objects.filter(plan_purched_at__date = today).aggregate(total_plan_price_amount = Sum('plan_price_amount'))
	totalsales = PlanPurchedByUser.objects.aggregate(total_plan_price_amount = Sum('plan_price_amount'))
	totalPlus=PlanPurchedByUser.objects.filter(plan_name__startswith="Plus").count()
	totalSuper=PlanPurchedByUser.objects.filter(plan_name__startswith="Super").count()
	
    
	return render(request,'homepage.html',{
	'todayuser':todayusers,
	'totaluser':totaluser,
    'todaysale':todaysales,
    'totalsale':totalsales,
    'todayMatchs':todayMatch,
    'totalMatchs':totalMatch,
    'totalPluss':totalPlus,
    'totalSupers':totalSuper

	})

def userList(request):
    user = Users.objects.filter(active = True)
    page = request.GET.get('page', 1)
    paginator = Paginator(user, 2)
    try:
        userlists = paginator.page(page)

    except PageNotAnInteger:
        userlists = paginator.page(1)
    except EmptyPage:
        userlists = paginator.page(page.num_pages)
    
    return render(request, 'userlisting.html', {'users':user,'userlists':userlists})
def Detailsuser(request, id):
    user = Users.objects.get(id = id)
    print(user)
    return render(request, 'detailsuser.html', {'user': user})

def userUpdate(request, id):
    obj = Users.objects.get(pk = id)    
    form = userForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('/userlist')   
    return render(request, 'userupdate.html', {'form': obj})

def blockuser(request, id):
    user = Users.objects.get(pk = id)
    user.active = False
    user.save()
    return redirect('/userList')
def unblockuser(request, id):
    user = Users.objects.get(pk = id)
    user.active = True
    user.save()
    return redirect('/unblockuser')

def blockUserslist(request):
    user = Users.objects.filter(active = False)
    page = request.GET.get('page', 1)
    paginator = Paginator(user, 2)
    try:
        blocks = paginator.page(page)

    except PageNotAnInteger:
        blocks = paginator.page(1)
    except EmptyPage:
        blocks = paginator.page(page.num_pages)
    return render(request, 'blockuserlist.html', {'users':user,'blocks':blocks})

def searchUser(request):
    if request.method == 'POST':
        data = request.POST['q']
        # data = request.POST['datejoined']
        print(data)
        user  = Users.objects.filter(dob__icontains= data) or Users.objects.filter(phone_no__icontains= data) or Users.objects.filter(email__icontains= data) or Users.objects.filter(gender__icontains= data) or Users.objects.filter(id__icontains= data)

        return render(request, 'userlisting.html', {'users':user})
def planpurchedbyuser(request):
    PlanPurchedBy = PlanPurchedByUser.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(PlanPurchedBy, 2)
    try:
        subs = paginator.page(page)

    except PageNotAnInteger:
        subs = paginator.page(1)
    except EmptyPage:
        subs = paginator.page(page.num_pages)
    
    return render(request, 'userSubscriptions.html', 
        {'PlanPurchedByuser':PlanPurchedBy,
        'subs':subs}
        )

def planpurchedbyuserDetails(request, id):
    user = PlanPurchedByUser.objects.get(id = id)
  
    return render(request, 'userSubscriptionDetails.html', 
        {'planpurchedbyUserDetail':user}
        )
def matchedprofiles(request):
    matchpro=Match.objects.all()
    return render(request, 'matched.html', {'users':matchpro})
def Matchprofiles(request, id):
    matcheddel = Match.objects.get(id = id)
    matcheddel.delete()
    return redirect('/matchedprofiles')
def Reported(request):
    Report=Reports.objects.all()
    return render(request,'report.html',{'Reports':Report})
def deleteReported(request, id):
    Reporteddel = Reports.objects.get(id = id)
    Reporteddel.delete()
    return redirect('/Reported')
def paytmpaymentStatus(request):
    PaytmPayment=PaytmPaymentStatus.objects.all()
    return render(request,'paymentstatus.html',
        {'paytmpayment':PaytmPayment}
        )
def ordermanagement(request):
    order=PurchaseRequest.objects.all()
    return render(request, 'ordermanage.html', {'order':order})
def ordermanagementDetails(request, id):
    user = PurchaseRequest.objects.get(id = id)
   
    return render(request, 'orderdetails.html', 
        {'planpurchedbyUserDetail':user}
        )

def userListCSV(request):

    # Get all data from UserDetail Databse Table
    users = Users.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="userlist.csv"'

    writer = csv.writer(response)
    writer.writerow(['User ID', 'Username', 'Phone', 'DOB','Created Date'])

    for user in users:
        writer.writerow([user.id, user.user,  user.phone_no,user.dob,user.create_at])

    return response
def datefilter(request):
    if request.method == 'POST':
        data = request.POST['start']
        print(data)
        user  = Users.objects.filter(create_at__icontains= data)  

        return render(request, 'userlisting.html', {'users':user})
