from django.conf.urls import url, include
from . import views
from addresources.models import addresources, addmatchingresources, editresources
app_name = 'addresources'
urlpatterns = [
    url(r'^addresources/$', views.create_addresources, name='create_addresources'),
    url(r'^editresources/$', views.editresourcesCreate, name='editresourcesCreate'),
    url(r'^(?P<addresources_id>[0-9]+)/details/$', views.details, name='details'),
    url(r'^(?P<addresources_id>[0-9]+)/visitor/$', views.visitor, name='visitor'),
    url(r'^(?P<addresources_id>[0-9]+)/addmatchingresources/$', views.addmatchingresourcesCreate, name='addmatchingresourcesCreate'),
    url(r'^(?P<addresources_id>[0-9]+)/delete_matches/(?P<addmatchingresources_id>[0-9]+)/$', views.delete_matches, name='delete_matches'),
    url(r'^(?P<addresources_id>[0-9]+)/delete_addresources/$', views.delete_addresources, name='delete_addresources'),
    url(r'^(?P<addresources_id>[0-9]+)/addresources_update/$', views.addresources_update, name='addresources_update'),
    url(r'^(?P<addresources_id>[0-9]+)/technologyCreate/(?P<addmatchingresources_id>[0-9]+)/$', views.technologyCreate, name='technologyCreate'),
    url(r'^(?P<addresources_id>[0-9]+)/technologyDetails/(?P<addmatchingresources_id>[0-9]+)/$', views.technologyDetails, name='technologyDetails'),
    url(r'^(?P<addresources_id>[0-9]+)/technologyUpdate/(?P<addmatchingresources_id>[0-9]+)/(?P<technologies_id>[0-9]+)$', views.technology_update, name='technology_update'),
    url(r'^dfs/$', views.dfs, name='dfs'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]
