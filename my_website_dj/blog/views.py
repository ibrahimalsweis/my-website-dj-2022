from django.shortcuts import render 
from .models import Post


def index (request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context)



def new_post (request):
    return render(request,'blog/new-post.html')