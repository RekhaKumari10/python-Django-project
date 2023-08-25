from distutils.log import Log
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

# def lform(request):
#     var_form = Login()
#     if request.method == 'POST':
#         data={}
#         var_form = Login(request.POST)
#         if var_form.is_valid():
#             email = var_form.cleaned_data['email']
#             phone = var_form.cleaned_data['phone']

#             data['email'] = email 
#             data['phone'] = phone 

#             Login_Details(email=email , phone=phone).save()
#         return render(request,'index.html',{'form':data})
#     else:
#         return render(request,'index.html',{'fm':var_form})

def index(request):
    return render(request,'index.html')
def wedding(request):
    return render(request, 'wedding.html')
def birthday(request):
    return render(request, 'birthday.html')
def contact(request):
    return render(request, 'contact.html')
def booking(request):
    return render(request, 'booking.html')        


# def login(request):
#     return render(request,'login.html')
# def sign_up(request):
#     return render(request,'sign_up.html')

def validation(request):
    if request.method =='POST':
        fname=request.POST['first_name']
        lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        Register(FName=fname,LName=lname,Email=email,Password=password).save()
    else:
        return HttpResponse("404 ERROR")
    return render(request,'index.html',{})

def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
   
    modelobj = Register.objects.all()
    isvalid = False
    for i in modelobj:
        if((i.Email==email)or(i.Password==password)):
            isvalid = True
    if(isvalid):
        return HttpResponse("Login Successfully")
    else:
        return HttpResponse("Please enter valid info")