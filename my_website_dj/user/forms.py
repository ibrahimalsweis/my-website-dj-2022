
from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):

    username = forms.CharField(max_length=99)
    first_name = forms.CharField(max_length=99,label='ألاسم الاول')
    last_name = forms.CharField(max_length=99 ,label='ألاسم الاخير')
    password1 = forms.CharField(min_length=8,label='كلمة المرور ')
    password2= forms.CharField(min_length=8,label='تأكيد كلمة المرور ')
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password']

        widgets ={
            'password2':forms.TextInput(attrs={'class':"form-control"})
        }