
from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import UserCreationForm
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

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             new_user = form.save(commit=False)
#             username = form.cleaned_data['username']
#             # new_user.set_password(form.cleaned_data['password1'])
#             # new_user.save()

#             messages.success(
#                 request, f'تهانينا {new_user} لقد تمت عملية التسجيل بنجاح.')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'user/register.html', {
#         'title': 'التسجيل',
#         'form': form,
#     })
