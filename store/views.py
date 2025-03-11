from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to My E-Commerce Site!</h2>")

