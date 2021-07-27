from django.urls import path
from app.views import *
from . import views

urlpatterns = [
    path('',Home.as_view(),name='home'),
]