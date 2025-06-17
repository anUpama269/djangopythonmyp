from django.shortcuts import render

#home view
from django.http import HttpResponse
def home(request):
    context={'name':'Arun','age':25,'place':'Tvm'}
    #return HttpResponse("Welcome to home")
    return render(request,'home.html',context)

#first page view
def first(request):
   #return HttpResponse("First Page")
   return render(request,'first.html')
#second page view
def second(request):
    #return HttpResponse("Second Page")
    return render(request,'second.html')
