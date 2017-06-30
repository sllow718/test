from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import getinformation
from .forms import getinformationForm
  
def getinformationCreate(request):
    form = getinformationForm(request.POST or None)
    return render(request, 'getinformation/getinformation_form.html', {'form':form})
