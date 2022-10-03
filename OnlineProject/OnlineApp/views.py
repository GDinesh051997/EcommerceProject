from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def Products(request):
    return render(request,"elements.html")

def Index(request):
    return render(request,"index.html")

def Contact(request):
    return render(request,"contact.html")

def Destination(request):
    return render(request,"destinations.html")

def News(request):
    return render(request,"news.html")