from django.shortcuts import render

def third(request):
   #return HttpResponse("First Page")
   return render(request,'third.html')
#second page view
def fourth(request):
    #return HttpResponse("Second Page")
    return render(request,'fourth.html')
