from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_worksmanager = models.BooleanField(default=False)
    is_customer = models.BooleanField(default =False)


class Customer(models.Model):
    User = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='customer')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    document = models.FileField(upload_to='document/')


    def __str__(self):
        return self.name

class Worksmanager(models.Model):
    User = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='manager')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()
    employee_id = models.CharField(max_length=4)
    document = models.FileField(upload_to='document/')

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    feedback =models.TextField()
    date = models.DateField(auto_now=True)
    reply = models.TextField(null=True,blank=True)

class Schedule(models.Model):
    date = models.DateField()
    starting_time = models.TimeField()
    ending_time = models.TimeField()
    status = models.BooleanField(default=0)

class Booking(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    schedule = models.ForeignKey(Schedule,on_delete=models.DO_NOTHING)
    status = models.IntegerField(default=0)


class Admin_Work_Create(models.Model):
    worksmanager = models.ForeignKey(Worksmanager, on_delete=models.DO_NOTHING)

    cat = (('two wheeler with gear','two wheeler with gear'),('two wheeler without gear','two wheeler without gear'),
           ('three wheeler','three wheeler'),('four wheeler','four wheeler'))
    category = models.CharField(max_length=50,choices=cat,null=True,blank=True)
    vehicle_no = models.PositiveIntegerField(null=True,blank=True)
    vehicle_name = models.CharField(max_length=100,null=True,blank=True)
    vehicle_model = models.CharField(max_length=100, null=True, blank=True)
    vehicle_brand = models.CharField(max_length=100, null=True, blank=True)
    problem_description = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now=True,null=True,blank=True)
    cost = models.PositiveIntegerField(null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING,null=True)
    stat = (('repairing','repairing'),('repairing done','repairing done'),('released','released'))
    status = models.CharField(max_length=100,choices=stat,default='Pending',null=True,blank=True)
    pay  = models.IntegerField(default=0)


class CustomerPayment(models.Model):
    data = models.ForeignKey(Admin_Work_Create,on_delete=models.DO_NOTHING)
    card_number = models.CharField(max_length=16)
    cvv = models.CharField(max_length=3)
    expiry_date = models.CharField(max_length=5)
