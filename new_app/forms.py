import datetime

from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserCreationForm


from new_app.models import Login, Customer, Worksmanager, Feedback, Schedule, Admin_Work_Create, CustomerPayment


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirmpassword", widget=forms.PasswordInput)
    class Meta:
        model =  Login
        fields = ('username','password1','password2')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('User',)

class WorksmanagerForm(forms.ModelForm):
    class Meta:
        model = Worksmanager
        exclude = ('User',)


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('feedback',)


class DateInput(forms.DateInput):

    input_type = 'date'

class TimeInput(forms.TimeInput):

    input_type = 'time'

class ScheduleForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    starting_time = forms.TimeField(widget=TimeInput)
    ending_time = forms.TimeField(widget=TimeInput)

    class Meta:
        model = Schedule
        fields =('date','starting_time','ending_time')

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("starting_time")
        end = cleaned_data.get("ending_time")
        date = cleaned_data.get("date")
        if start > end:
            raise forms.ValidationError("end time should be greater than start time")
        if date < datetime.date.today():
            raise forms.ValidationError("date cant be in the past")
        return cleaned_data

class Admin_Work_Assain(forms.ModelForm):
    class Meta:
        model = Admin_Work_Create
        exclude = ('customer',)

class  Manager_Work_Update(forms.ModelForm):
    class Meta:
        model = Admin_Work_Create
        exclude = ('worksmanager','customer',)


class PaymentForm(forms.ModelForm):
    expiry_date = forms.CharField(label = 'Expiry Date(MM/YY)',
                                  max_length=5, required=True,widget=forms.TextInput(attrs={'placeholder': '(MM/YY)'}))
    cvv = forms.CharField(max_length=3,widget=forms.TextInput(attrs={'placeholder':'CVV'}))
    card_number = forms.CharField(max_length=16,widget=forms.TextInput(attrs={'placeholder':'CARD NUMBER'}))
    class Meta:
        model = CustomerPayment
        exclude = ('data',)





