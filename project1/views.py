from django import http
from django.shortcuts import render

def Index(request):
    print("client request is :- ",request)
    return http.HttpResponse("helloworld")

def sample(request):
    return http.HttpResponse("<marquee><big>HELLO UNIVERSE</big></marquee>")

def home(request):
    return render(request,"home.html")

