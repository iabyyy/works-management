from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import LoginForm, CustomerForm, WorksmanagerForm
from new_app.models import Worksmanager, Customer


# Create your views here.
def test(request):
    return render(request,'index.html')



def dash(request):
    return render(request,'dash.html')






def customer_reg(request):
    form1 = LoginForm()
    form2 = CustomerForm()
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = CustomerForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_customer = True
            user1.save()
            user2 = form2.save(commit = False)
            user2.User=user1
            user2.save()
            return redirect('home')
    return render(request,'customer_register.html',{ 'form1':form1, 'form2':form2 })



def manager_reg(request):
    form1 = LoginForm()
    form2 = WorksmanagerForm()
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        form2 = WorksmanagerForm(request.POST,request.FILES)
        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_worksmanager = True
            user1.save()
            user2 = form2.save(commit=False)
            user2.User=user1
            user2.save()
            return redirect('adminpage')
    return render(request,'manager/manager_register.html',{'form1':form1, 'form2':form2})





def login_view(request):
    if request.method =='POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
            if user.is_worksmanager:
                return redirect('profile_view')
            if user.is_customer:
                return redirect('customer_profile')

        else:
            messages.info(request,'invalid credentials')
    return render(request,'stafflogin.html')
@login_required(login_url='user')
def staffpage(request):
    return render(request,'admin/adminpage.html')

@login_required(login_url='user')
def customerpage(request):
    u = request.user
    cust = Customer.objects.get(User=u)

    return render(request,'customer/customerpage.html',{'cust':cust})

@login_required(login_url='user')
def managerpage(request):
    return render(request,'manager/managerpage.html')

@login_required(login_url='user')
def managertable(request):
    data = Worksmanager.objects.all()
    return render(request,'manager/managertable.html',{'view':data})

@login_required(login_url='user')
def managerdelete(request,id):
    data = Worksmanager.objects.get(id=id)
    data.delete()
    return redirect('managertable')

@login_required(login_url='user')
def managerupdate(request,id):
    data = Worksmanager.objects.get(id=id)
    form = WorksmanagerForm(instance=data)
    if request.method=='POST':
        data = WorksmanagerForm(request.POST,request.FILES,instance=data)
        if data.is_valid():
            data.save()
            return redirect('managertable')
    return render(request,'manager/managerupdate.html',{'update':form})

@login_required(login_url='user')
def customertable(request):
    data = Customer.objects.all()
    return render(request,'customer/customertable.html',{'cust':data})

@login_required(login_url='user')
def customerdelete(request,id):
    data = Customer.objects.get(id=id)
    data.delete()
    return redirect('customertable')




