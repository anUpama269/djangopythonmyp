from django.shortcuts import render

#home view
from django.http import HttpResponse
def home(request):


  return HttpResponse("Django")

#index view
def index(request):
  return HttpResponse("Index page")
