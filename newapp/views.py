from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.conf import settings
from . models import *
import random
from paintapp.models import Upload
from paintapp.models import Order
# Create your views here.

def index(request):
    return render(request,'newtmplt/index.html')
def four(request):
    return render(request,'newtmplt/404.html')
def blank(request):
    return render(request,'newtmplt/blank.html')
def buttontmplt(request):
    return render(request,'newtmplt/button.html')
def chart(request):
    return render(request,'newtmplt/chart.html')
def element(request):
    return render(request,'newtmplt/element.html')
def form(request):
    return render(request,'newtmplt/element.html')
def signin(request):
    return render(request,'newtmplt/signin.html')
def signup(request):
    return render(request,'newtmplt/signup.html')
def table(request):
    return render(request,'newtmplt/table.html')
def typography(request):
    return render(request,'newtmplt/typography.html')
def widget(request):
    return render(request,'newtmplt/widget.html')
def otp(request):
    return render(request,'newtmplt/otp.html')
def password(request):
    return render(request,'newtmplt/password.html')

def paintsignup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        random_number= random.randint(100000,999999)
        subject='painting - your verification code'
        message=f'your OTP is {random_number}. It is valid for 5 minutes.'
        send_mail(subject,message,settings.EMAIL_HOST_USER,[email],fail_silently=False)
        india_time = timezone.localtime(timezone.now())
        CustomUser.objects.create_user(username=name,name=name,email=email,otp=random_number,exp_timee=india_time + timedelta(minutes=335))
        request.session['name']=name
        return redirect('newapp:otp')
     
   
def newotp(request):
    if request.method=='POST':
        input1=request.POST.get('input1')
        input2=request.POST.get('input2')
        input3=request.POST.get('input3')
        input4=request.POST.get('input4')
        input5=request.POST.get('input5')
        input6=request.POST.get('input6')
        print(input1,input2,input3,input4,input5,input6)
        my_otp=str(input1)+str(input2)+str(input3)+str(input4)+str(input5)+str(input6)
        name=request.session['name']
        user=CustomUser.objects.get(username=name)
        otp=user.otp
        exp=user.exp_timee
        print(otp,my_otp,'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
        if otp==int(my_otp) and exp>timezone.now()+timedelta(minutes=330):
          return redirect('newapp:password')
        else:
            messages.success(request,'invalid otp')
            return redirect('newapp:otp')
def newpass(request):
    if request.method=='POST':
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        name=request.session['name']
        user=CustomUser.objects.get(username=name)
        user.password=password
        user.save()
        print(password,confirmpassword)
        return redirect('newapp:signin')
def signinsave(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(email,password)
        user=CustomUser.objects.get(email=email,password=password)
        # user=authenticate(request,email=email,password=password)
        if user:
            login(request,user)
            return redirect('paintapp:index')
        else:
            messages.error(request,'incorrect password')
            return redirect('newapp:signin')
def viewuser(request):
    user= CustomUser.objects.filter(is_superuser=False)
    context={
        'user':user
    }

    return render(request,'newtmplt/viewuser.html',context)
def viewdetails(request,im_id):
    viewuser=CustomUser.objects.get(id=im_id)
    context={
        'viewuser':viewuser
    }

    return render(request,'newtmplt/viewdetails.html',context)

def viewwork(request,item_id):
    user=CustomUser.objects.get(id=item_id)
    works=Upload.objects.filter(user=user)
   
    context={
        'works':works
    }
    return render(request,'newtmplt/viewwork.html',context)
def viewpurchase(request,item_id):
    viewuser = CustomUser.objects.get(id=item_id) 
    arts = Order.objects.filter(user=viewuser)
    total_art_count = arts.count()
    context={
       'viewuser':viewuser,
        'arts': arts,
        'total_art_count': total_art_count
    }

    return render(request,'newtmplt/viewpurchase.html',context)
   



