from django.http import HttpResponse
from django.shortcuts import render
from home.models import Contect
# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
   # return HttpResponse("This is my aboutpage")
    return render(request,'about.html')

def projects(request):
   # return HttpResponse("This is my projectspage")
    return render(request,'projects.html')

def contect(request):
     if request.method=="POST":
         name=request.POST['name']
         email=request.POST['email']
         phone=request.POST['phone']
         desc=request.POST['desc']
         print(name,email,phone,desc)
         ins=Contect(name=name,email=email,phone=phone,desc=desc)
         ins.save()
         print("This is after models")
     return render(request,'contect.html')