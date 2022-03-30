

import email
from turtle import textinput
from django import forms
from django.contrib.auth.models import User
from .models import Profile
class UserCreationForm(forms.ModelForm):

    username = forms.CharField(max_length=99,label='أسم المستخدم ',widget=forms.TextInput(attrs={'class':"form-control mt-2"}))
    first_name = forms.CharField(max_length=99,label='ألاسم الاول',widget=forms.TextInput(attrs={'class':"form-control mt-2 mt-2"}))
    email = forms.CharField(max_length=99,label='البريد الألكتروني',widget=forms.EmailInput(attrs={'class':"form-control mt-2"}))
    last_name = forms.CharField(max_length=99 ,label='ألاسم الاخير',widget=forms.TextInput(attrs={'class':"form-control mt-2"}))
    password1 = forms.CharField(min_length=8,label='كلمة المرور ' , widget=forms.PasswordInput(attrs={'class':"form-control mt-2"}))
    password2= forms.CharField(min_length=8,label='تأكيد كلمة المرور ',widget=forms.PasswordInput(attrs={'class':"form-control mt-2"}))
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']


    def clean_password2(self):
        c_data = self.cleaned_data
        if c_data['password1'] != c_data['password2']:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        return c_data['password2']

    def clean_username(self):
        c_data = self.cleaned_data
        if User.objects.filter(username=c_data['username']).exists():
            raise forms.ValidationError("اسم المستخدم  موجود بالفعل ")
        return c_data['username']




class UserForm_update(forms.ModelForm):
    first_name = forms.CharField(max_length=99,label='ألاسم الاول')
    last_name = forms.CharField(max_length=99 ,label='ألاسم الاخير')
    email = forms.EmailField(label='البريد الالكتروني')
    class Meta:
        model =  User
        fields = ('first_name','last_name','email','username')

class ProfileForm_update(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = ('img',)
