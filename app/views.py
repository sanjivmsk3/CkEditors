from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, ListView
from app.models import *
# Create your views here.
from app.forms import PostForm


class Home(ListView):
    def get(self,request):
        forms = PostForm(request.POST)
        contxt = {
            'form': forms,
            'post':Post.objects.all()
        }
        return render(request,'home.html',contxt)

    def post(self,request):
        forms =PostForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            forms.save()
            return redirect('home')
