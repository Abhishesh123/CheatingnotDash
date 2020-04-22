from django.shortcuts import render,redirect
import datetime
from django.contrib.sessions.models import Session
from userprofile.models import Users,Match,Reports
from subscription.models import PlanPurchedByUser,PaytmPaymentStatus,PurchaseRequest
from django.utils import timezone
from dashboard.forms import  userForm
from django.db.models import Sum,Count

# Create your views here.

def Index(request):
	today      = datetime.date.today()
	todayusers = Users.objects.filter(create_at__date=today).count()
    # todaysales = PlanPurchedByUser.objects.filter(plan_purched_at__date=today).aggregate(total_plan_price_amount=Sum('plan_price_amount'))
    # totalsales = PlanPurchedByUser.objects.aggregate(total_plan_price_amount=Sum('plan_price_amount'))
	totaluser  = Users.objects.all().count()
    
	return render(request,'homepage.html',{
	'todayuser':todayusers,
	'totaluser':totaluser
    # 'todaysale':todaysales,
    # 'totalsale':totalsales

	})

def userList(request):
    user = Users.objects.filter(active = True)
    return render(request, 'userlisting.html', {'users':user})
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
    return render(request, 'blockuserlist.html', {'users':user})

def searchUser(request):
    if request.method == 'POST':
        data = request.POST['q']
        # data = request.POST['datejoined']
        print(data)
        user  = Users.objects.filter(dob__icontains= data) or Users.objects.filter(phone_no__icontains= data) or Users.objects.filter(email__icontains= data) or Users.objects.filter(gender__icontains= data) or Users.objects.filter(id__icontains= data)

        return render(request, 'userlisting.html', {'users':user})
def planpurchedbyuser(request):
    PlanPurchedBy = PlanPurchedByUser.objects.all()
    
    return render(request, 'userSubscriptions.html', 
        {'PlanPurchedByuser':PlanPurchedBy}
        )

def planpurchedbyuserDetails(request, id):
    user = PlanPurchedByUser.objects.get(id = id)
    print(user)
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
def paytmpaymentStatus(request):
    PaytmPayment=PaytmPaymentStatus.objects.all()
    return render(request,'paymentstatus.html',
        {'paytmpayment':PaytmPayment}
        )
def ordermanagement(request):
    order=PurchaseRequest.objects.all()
    return render(request, 'ordermanage.html', {'order':order})
