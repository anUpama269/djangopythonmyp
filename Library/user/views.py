from django.shortcuts import render,redirect
from django.views import View
from user.forms import SignupForm
from user.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.core.mail import send_mail
# def register(request):
#     return render(request,'register.html',)
# def login(request):
#     return render(request,'login.html',)
# def logout(request):
#     return render(request,'logout.html',)

class RegisterView(View):
    def get(self, request):
        form_instance=SignupForm()
        return render(request,'register.html',{'form':form_instance})
    def post(self,request):
         form_instance=SignupForm(request.POST)
         if form_instance.is_valid():
             user=form_instance.save(commit=False)
             user.set_password(form_instance.cleaned_data['password'])
             user.save()
             user.generate_otp()

             send_mail(
                 "Django Auth OTP",
                 user.otp,
                 "anupoachu99921@gmail.com",
                 ["mailtoanupamapnair@gmail.com"],
                 fail_silently=False,
             )
             return redirect('user:OtpVerificationView')




class LoginView(View):
    def get(self,request):
        form_instance=LoginForm()
        return render(request,'login.html',{'form':form_instance})
    def post(self,request):
        form_instance=LoginForm(request.POST)
        if form_instance.is_valid():
            name=form_instance.cleaned_data['username']
            pwd=form_instance.cleaned_data['password']
            # print(name,pwd)
            user=authenticate(username=name,password=pwd)
            if user:
                login(request,user)
                u=request.user
                print(u.username)
                print(u.email)
                print(u.last_name)
                return redirect('books:home')
            else:
                print('invalid user credential')
                return redirect('user:login')


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('books:home')




from django.contrib import messages
from user.models import CustomUser
class OtpVerificationView(View):
    def get(self, request):
        return render(request,'otp_verify.html')
    def post(self,request):
        otp=request.POST['otp']
        try:
            u = CustomUser.objects.get(otp=otp)
            u.is_active = True
            u.is_verified = True
            u.otp = None
            u.save()
            return redirect('SigninView')
        except:
            messages.error(request, "Invalid OTP")
            return redirect('OtpVerificationView')
