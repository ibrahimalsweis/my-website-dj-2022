from multiprocessing import context
from django.shortcuts import render
from .forms import UserCreationForm
# Create your views here.

def register(request):
    form =UserCreationForm()
    context={
        'form':form
    }
    return render(request,'user/register.html',context)