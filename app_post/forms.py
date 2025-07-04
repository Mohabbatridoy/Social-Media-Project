from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('image','caption',)
        
class commentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Write a comment...','label':None}),
        }