from pyexpat import model
from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post , Comment
from .forms import NewComment , CreateFormPost
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView ,UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
def index (request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/index.html',context)




@login_required(login_url='login')
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


class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    # fields = ['content_post']
    template_name = 'blog/new-post.html'
    form_class = CreateFormPost 
    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)

class UpdatePostView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    # fields = ['content_post']
    model = Post
    template_name = 'blog/update_post.html'
    form_class = CreateFormPost 
    def form_valid(self, form):
        form.instance.auth = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()

        if self.request.user == post.auth:
            return True
        return False

class DeletePostView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.auth:
            return redirect('index')
        return False