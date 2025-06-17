
from django.shortcuts import render
from app1.forms import AdditionForm
def addition(request):
    if request.method == 'POST':
        print(request.post)
        return render(request,'Addition.html')



    form_instance = AdditionForm()
    return render(request,'Addition.html',{'form':form_instance})

#Factorial
from app1.forms import FactorialForm
def factorial(request):
    if request.method == 'POST':
        print(request.POST)
    form_instance = FactorialForm()
    return render(request, 'factorial.html',{'form':form_instance})


#BMI
from app1.forms import BMIForm
def bmi(request):
    if request.method == 'POST':
        print(request.POST)
        # GET Request
    form_instance = BMIForm()
    return render(request, 'bmi.html',{'form':form_instance})
from app1.forms import SignupForm
def signup(request):

    if request.method == "POST":
        return render(request, 'bmi.html')

    form_instance = SignupForm()
    return render(request, 'signup.html',{'form':form_instance})

from app1.forms import CalorieForm
def caloriecalculator(request):
    if request.method == "POST":
        print(request.POST)
        form_instance=CalorieForm(request.POST)
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            weight=float(data['Weight'])
            height=float(data['Height'])
            age=int(data['Age'])
            gender=data['gender']
            activity_level=float(data['Activity'])
            print(weight,height,age,gender,activity_level)

            print(data)

            if gender=='female':
                BMR=((10*weight+6.25*height)-(5*age))-161
                calorie=BMR*activity_level
                print(calorie)
            else:
                BMR = ((10 * weight + 6.25 * height) - (5 * age)) + 5
                calorie = BMR * activity_level
                print(calorie)

        return render(request,'caloriecalculator.html',{'form':form_instance,'result':calorie})

    form_instance = CalorieForm()
    return render(request, 'caloriecalculator.html',{'form':form_instance})