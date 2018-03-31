from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('title', 'text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ('text',)
        labels = {'text': 'Comment'}
        widgets = {
            'text': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }