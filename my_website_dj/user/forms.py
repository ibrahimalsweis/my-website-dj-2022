
from cProfile import label
from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):

    # username = forms.CharField(max_length=99,label='أسم المستخدم ')
    # first_name = forms.CharField(max_length=99,label='ألاسم الاول')
    # last_name = forms.CharField(max_length=99 ,label='ألاسم الاخير')
    # password1 = forms.CharField(min_length=8,label='كلمة المرور ' , widget=forms.PasswordInput())
    # password2= forms.CharField(min_length=8,label='تأكيد كلمة المرور ',widget=forms.PasswordInput())
    # class Meta:
    #     model = User
    #     fields = ['username','email','first_name','last_name','password1','password2']

    # def clean_password2(self):
    #     c_data = self.cleaned_data
    #     if c_data['password1'] != c_data['password2']:
    #         raise forms.ValidationError('كلمة المرور غير متطابقة')
    #     return c_data['password2']

    # def clean_username(self):
    #     c_data = self.cleaned_data
    #     if User.objects.filter(username=c_data['username']).exists():
    #         # raise forms.ValidationError("اسم المستخدم  موجود بالفعل ")
    #         raise forms.ValidationError(("This username has already existed."))
    #     return c_data['username']


        
        username = forms.CharField(label='اسم المستخدم', max_length=30)
        email = forms.EmailField(label='البريد الإلكتروني')
        first_name = forms.CharField(label='الاسم الأول')
        last_name = forms.CharField(label='الاسم الأخير')
        password1 = forms.CharField(
            label='كلمة المرور', widget=forms.PasswordInput(), min_length=8)
        password2 = forms.CharField(
            label='تأكيد كلمة المرور', widget=forms.PasswordInput(), min_length=8)

        class Meta:
            model = User
            fields = ('username', 'email', 'first_name',
                    'last_name', 'password1', 'password2')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password1'] != cd['password2']:
                raise forms.ValidationError('كلمة المرور غير متطابقة')
            return cd['password2']

        def clean_username(self):
            cd = self.cleaned_data
            if User.objects.filter(username=cd['username']).exists():
                raise forms.ValidationError('يوجد مستخدم مسجل بهذا الاسم.')
            return cd['username']