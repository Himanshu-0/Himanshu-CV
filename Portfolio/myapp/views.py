from django.shortcuts import render
from .models import mymessage
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about_me.html')
def contact(request):
    if request.method=="POST": 
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        company=request.POST.get('company')
        message=request.POST.get('message')
        obj1=mymessage(name=name,email=email,mobile=mobile,company=company,message=message) 
        obj1.save() 
    return render(request, 'hire.html')
def edu(request):
    return render(request, 'education.html')
def exp(request):
    return render(request, 'experience.html')
def skill(request):
    return render(request, 'skills.html')
def certi(request):
    return render(request, 'certification.html')
def project(request):
    return render(request, 'project.html')