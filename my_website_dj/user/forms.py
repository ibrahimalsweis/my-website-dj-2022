
from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):

    username = forms.CharField(max_length=99,label='أسم المستخدم ')
    first_name = forms.CharField(max_length=99,label='ألاسم الاول')
    last_name = forms.CharField(max_length=99 ,label='ألاسم الاخير')
    password1 = forms.CharField(min_length=8,label='كلمة المرور ' , widget=forms.PasswordInput())
    password2= forms.CharField(min_length=8,label='تأكيد كلمة المرور ',widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']

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


        
