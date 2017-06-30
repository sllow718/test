from django.shortcuts import render
from addresources.models import addresources
from updatelog import views

#from django.contrib.auth import authenticate, login
#from django.views.generic import View
#from .forms import UserForm

#class UserFormView(View):
    #form_class = UserForm
    #template_name = 'webapp/registration.html'

def index(request):
    return render(request, 'webapp/home.html') # this two parameters are compulsory

def database(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/database.html', {'all_resources':all_resources})

def filter(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/filter.html', {'all_resources':all_resources})

def calculator(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/calculator.html', {'all_resources':all_resources})

def homepage(request):
    return render(request, 'webapp/homepage.html')

def filtervisitor(request):
    all_resources=addresources.objects.all()
    return render(request, 'webapp/filtervisitor.html', {'all_resources':all_resources})

def contact(request):
    return render(request, 'webapp/contactus.html')

def updatelog(request):
    return render(request, 'updatelog/about.html')
