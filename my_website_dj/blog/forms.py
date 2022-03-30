
from django import forms 
from blog.models import Comment
from .models import Post

class NewComment(forms.ModelForm):
    username = forms.CharField(max_length=99,label='أسم المستخدم ',widget=forms.TextInput(attrs={'class':"form-control mt-2"}))
    content_comment = forms.CharField(max_length=99,label='التعليق ',widget=forms.TextInput(attrs={'class':"form-control mt-2"}))
    email = forms.CharField(max_length=99,label='البريد الألكتروني',widget=forms.EmailInput(attrs={'class':"form-control mt-2"}))
    
    class Meta:
        model = Comment
        fields = ('username','content_comment','email')

        
class CreateFormPost(forms.ModelForm):
    content_post = forms.CharField(label='منشور جديد',widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['content_post']

