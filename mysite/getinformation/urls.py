from django.conf.urls import url, include
from . import views
from getinformation.models import getinformation
app_name = 'getinformation'
urlpatterns = [
    url(r'^$', views.getinformationCreate, name='getinformationCreate'),
]

