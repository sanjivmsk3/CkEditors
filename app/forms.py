from django import forms
from django.forms import ModelForm
from app.models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['desc']