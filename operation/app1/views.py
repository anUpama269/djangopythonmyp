from django.shortcuts import render

def addition(request):
    if request.method=='POST':
        print(request.POST)
        n1=request.POST['num']
        n2=request.POST['num2']
        result=int(n1)+int(n2)
        #print(result)
        context={'result':result,}
        return render(request,'Addition.html',context)



    return render(request,'Addition.html')
def factorial(request):
    if request.method == "POST":
        n1 = int(request.POST['num1'])
        result = 1
        for i in range(1, n1 + 1):
            result *= i
        context = {'result': result}
        return render(request, 'factorial.html', context)
        
    return render(request, 'factorial.html')
def bmi(request):
    if request.method == 'POST':
        weight = float(request.POST['w'])
        height = float(request.POST['h']) / 100
        bmi = weight / (height ** 2)
        context = {'result': bmi}
        return render(request, 'bmi.html', context)
    return render(request, 'bmi.html')

