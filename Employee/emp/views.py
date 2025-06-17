from django.shortcuts import render,redirect
from emp.forms import AddemployeeForm
from emp.models import Employe
def home(request):
    return render(request,'home.html')
def Addemployee(request):
    if request.method == "POST":
        form_instance=AddemployeeForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()

        return redirect("viewemployee")



    form_instance=AddemployeeForm()
    return render(request,'Add Employee.html',{'form':form_instance})
def viewemployee(request):
    e=Employe.objects.all()
    print(e)
    return render(request,'viewemployee.html',{'emp':e})

def detail_view(request,i):
    e = Employe.objects.get(id=i)
    return render(request,'detailemployee.html',{'emp':e})
#
def edit_view(request,i):
    e=Employe.objects.get(id=i)
    if request.method == "POST":
        form_instance = AddemployeeForm(request.POST, request.FILES, instance=e)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('viewemployee')
    form_instance = AddemployeeForm(instance=e)
    return render(request, 'editview.html', {'form': form_instance})


def deleteemployee(request, i):
    e = Employe.objects.get(id=i)
    e.delete()
    return redirect('viewemployee')




# Create your views here.
