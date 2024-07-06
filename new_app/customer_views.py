from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from new_app.forms import FeedbackForm, PaymentForm
from new_app.models import Customer, Feedback, Schedule, Booking, Admin_Work_Create, CustomerPayment

@login_required(login_url='user')
def customer_profile(request):
    u = request.user
    data = Customer.objects.filter(User=u)
    print(data)
    return render(request,'customer/customer_profile.html',{'customer_profile':data})

@login_required(login_url='user')
def customer_feed(request):
    data= request.user
    user= Customer.objects.get(User=data)
    data = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save( commit=False)
            obj.user= user
            obj.save()
    return render(request,'customer/custfeedback.html',{'customer_feed':data})

@login_required(login_url='user')
def customer_feedview(request):
    u =request.user.id
    data = Customer.objects.get(User=u)
    feedback = Feedback.objects.filter(user=data)
    return render(request,'customer/customer_feedview.html',{'feedview':feedback})
@login_required(login_url='user')
def customer_schedule(request):
    data = Schedule.objects.filter(status =0)
    return render(request,'customer/customer_schedule.html',{'customer_schedule':data})
@login_required(login_url='user')
def customer_booking(request,id):
    data = Schedule.objects.get(id=id)
    u = Customer.objects.get(User=request.user)
    appointment = Booking.objects.filter(user=u,schedule=data)
    if appointment.exists():
        messages.info(request,'booking slot already booked')
        return redirect("customer_schedule")
    else:
        if request.method =='POST':
            obj = Booking()
            obj.user = u
            obj.schedule=data
            obj.save()
            messages.info(request, ' slot  booked successfully')
            return redirect('customer_schedule')
    return render(request,'customer/customer_booking.html',{'customer_booking':data})
@login_required(login_url='user')
def bookingview(request):
    data = Booking.objects.all()
    return render(request,'customer/bookingview.html',{'view':data})
@login_required(login_url='user')
def vehiclestatus(request):
    u = request.user
    data = Customer.objects.get(User=u)
    form = Admin_Work_Create.objects.filter(customer=data)
    return render(request,'customer/vehiclestatus.html',{'vehiclestatus':form})
@login_required(login_url='user')
def payment(request,id):
    data = PaymentForm()
    user = Admin_Work_Create.objects.get(id=id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.data = user
            obj.save()
            user.pay  = 1
            user.save()
            print(user.pay)
            return redirect('vehiclestatus')
    return render(request,'customer/customer_payment.html',{'payment':data})





