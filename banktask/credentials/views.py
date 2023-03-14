from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('BUTTON')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password 1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)

                user.save();
                return redirect('login')
                messages.info(request, 'user created')
        else:
             messages.info(request,'password not matching')
             return redirect('register')
        return redirect('/')

    return render(request,'register.html')

def form(request):
    if request.method == 'POST':
        NAME=request.POST['NAME']
        DOB= request.POST['DOB']
        AGE = request.POST['AGE']
        GENDER = request.POST['GENDER']
        PHONE_NUMBER = request.POST['PHONE NUMBER']
        MAIL_ID = request.POST['MAIL ID']
        ADDRESS = request.POST['ADDRESS']

    # if User.objects.exists():
    #     messages.info(request, 'Application accepted')


    return render(request, 'form.html')

def BUTTON(request):

    return render(request,'BUTTON.html')