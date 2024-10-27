from django.shortcuts import render
from django.http import HttpResponse

def func(request):
    return render(request,"nanda.html")