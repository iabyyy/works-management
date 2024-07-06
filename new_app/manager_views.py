from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import Admin_Work_Assain, Manager_Work_Update
from new_app.models import Worksmanager, Booking, Admin_Work_Create


@login_required(login_url='user')
def profile_view(request):
    u = request.user
    print(u)
    data = Worksmanager.objects.filter(User= u)
    print(data)

    return render(request,'manager/profile_view.html',{'profile_view':data})

@login_required(login_url='user')
def manager_booking_approve(request):
    data = Booking.objects.all()
    return render(request,'manager/manager_booking.html',{'managerapprove':data})

@login_required(login_url='user')
def approval(request,id):
        data = Booking.objects.get(id=id)
        data.status = 1
        data.save()
        return redirect('manager_booking_approve')
@login_required(login_url='user')
def rejection(request,id):
    data = Booking.objects.get(id=id)
    data.status = 2
    data.save()
    return redirect('manager_booking_approve')

@login_required(login_url='user')
def managerwork(request):
    user = request.user.id
    customer =  Worksmanager.objects.get(User=user)

    data = Admin_Work_Create.objects.filter(worksmanager=customer)
    print(data)
    return render(request,'manager/managerworkassign.html',{'managerwork':data})

@login_required(login_url='user')
def managerworkupdate(request,id):
    data = Admin_Work_Create.objects.get(id=id)
    form = Manager_Work_Update(instance=data)
    if request.method =='POST':
        form =Manager_Work_Update(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('managerworkassign')
    return render(request,'manager/managerworkupdate.html',{'managerworkupdate':form})






