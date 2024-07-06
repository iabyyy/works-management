from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import ScheduleForm, Admin_Work_Assain
from new_app.models import Feedback, Schedule, Booking, Customer, Worksmanager, Admin_Work_Create

@login_required(login_url='user')
def adminfeedbackview(request):
    data = Feedback.objects.all()
    return render(request,'admin/adminfeedbackview.html',{'adminfeedback':data})

@login_required(login_url='user')
def feedupdate(request,id):
    feedback = Feedback.objects.get(id=id)
    if request.method == 'POST':
        r=request.POST.get('reply')
        feedback.reply = r
        feedback.save()
        messages.info(request,'reply send for feedback')
        return redirect('adminfeedbackview')
    return render(request,'admin/feedupdate.html',{'feedback':feedback})

@login_required(login_url='user')
def schedule(request):
    data = ScheduleForm()
    if request.method=='POST':
        form =ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'schedule added')
            return redirect('schedule_table')
        else:
            print(ScheduleForm.errors)
            messages.info(request, 'Please enter valid date and time')

    return render(request,'admin/schedule.html',{'schedule':data})
@login_required(login_url='user')
def schedule_table(request):
    data = Schedule.objects.filter(status = 0)
    return render(request,'admin/schedule_table.html',{'schedule':data})

def disable(request,id):
    data = Schedule.objects.get(id=id)
    data.status = 1
    data.save()
    return redirect("schedule_table")

@login_required(login_url='user')
def work_assaign(request):
    data = Booking.objects.filter(status = 1)
    return render(request,'admin/work_assaign.html',{'work_assaign':data})

@login_required(login_url='user')
def admin_work_create(request,id):
    user = Booking.objects.get(id=id)
    customer = user.user
    print(user.user)
    data = Admin_Work_Assain()
    if request.method=='POST':
        form = Admin_Work_Assain(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = customer
            obj.save()
        return redirect('work_assaign')
    return render(request,'admin/admin_work_create.html',{'work_create':data})







