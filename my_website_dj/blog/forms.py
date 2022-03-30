
from django import forms 
from blog.models import Comment
from .models import Post

class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','content_comment','email')

        
class CreateFormPost(forms.ModelForm):
    content_post = forms.CharField(label='منشور جديد',widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ['content_post']

