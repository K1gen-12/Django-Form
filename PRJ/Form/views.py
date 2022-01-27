from django.http import request
from django.shortcuts import render

# Create your views here.
def ShowHome(request):
    return render(request,'Home.html')