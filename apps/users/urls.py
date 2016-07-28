
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="login_page"),
	url(r'^login$', views.login, name="login"),
	url(r'^register$', views.register, name="register"),
	url(r'^logout$', views.logout, name="logout"),
]
