from django.conf.urls import url, include
from . import views
app_name = 'webapp'
urlpatterns = [
    url(r'^home/FAQ$', views.index, name='index'),
    url(r'^home/database$', views.database, name='database'),
    url(r'^home/searchadmin$', views.filter, name='filter'),
    url(r'^home/search$', views.filtervisitor, name='filtervisitor'),
    url(r'^home/calculator$', views.calculator, name='calculator'),
    url(r'^home/contact$', views.contact, name='contact'),
    url(r'^home', views.homepage, name='homepage')


    #url(r'^(?P<album_id>[0-9]+)$'), views.detail, name='detail'
]
