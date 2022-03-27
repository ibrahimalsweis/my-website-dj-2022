from django.shortcuts import render , get_object_or_404
from .models import Post , Comment
from .forms import NewComment

def index (request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context)


def new_post (request):
    return render(request,'blog/new-post.html')



def detail_post(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        form_comment = NewComment(data=request.POST)
        if form_comment.is_valid():
            new_comment = form_comment.save(commit=False)
            new_comment.post = post
            new_comment.save()
            form_comment = NewComment()
    else:        
        form_comment = NewComment()
    context ={
        'post':post,
        'comments':comments,
        'form_comment':NewComment()
    }




    return render(request,'blog/detail_post.html',context)