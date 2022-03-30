
from multiprocessing import context
from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import UserCreationForm , UserForm_update , ProfileForm_update
from django.contrib.auth import authenticate , login , logout
from blog.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            # new_user = form.cleaned_data['username']
            messages.success(request,f'مرحياً{new_user} تم أنشاء الحساب بنجاح يمكنك ألان تسجيل الدخول ')
            return redirect('login')
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
            return redirect('profile')
        else:
            messages.warning(request,f'هناك خطأ في البيانات')
    return render(request,'user/signIn.html',context={'form': 't'})


def logout_user(request):
    logout(request)
    return render(request,'user/logout.html')


@login_required(login_url='login')
def profile(request):
    posts = Post.objects.filter(auth=request.user)
    return render(request,'user/profile.html',context={'posts':posts})



def profile_update(request):
    if request.method == 'POST':
        user_form = UserForm_update(request.POST,instance=request.user)
        profile_form = ProfileForm_update(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():    
            user_form.save()
            profile_form.save()
            messages.success(request,'تم تعديل الملف الشخصي')
            return redirect('profile')
    else:
        user_form = UserForm_update(instance=request.user)
        profile_form = ProfileForm_update(instance=request.user.profile)

    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request,'user/profile_update.html',context)