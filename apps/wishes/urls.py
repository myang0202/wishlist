from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="dashboard"),
    url(r'^create$', views.additem, name ="additem"),
    url(r'^create_process$', views.create, name ="create"),
    url(r'^(?P<id>\d+)$', views.show, name="show_wish"),
    url(r'^addtolistlist/(?P<id>\d+)$', views.addtolist, name="addtolist"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    ]
