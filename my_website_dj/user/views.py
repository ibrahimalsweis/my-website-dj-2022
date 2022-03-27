
from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import UserCreationForm 
from django.contrib.auth import authenticate , login , logout
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request,f'مرحباً {username} تم أنشاء الحساب بنجاح')
            return redirect('index')
    else:
        form = UserCreationForm()

    context={
        'form':form
    }
    return render(request,'user/register.html',context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'مرحباً {username} تم تسجيل الدخول بنجاح')
            return redirect('index')
        else:
            messages.warning(request,f'هناك خطأ في البيانات')
    return render(request,'user/signIn.html',context={'form': 't'})


def logout_user(request):
    logout(request)
    return render(request,'user/logout.html')