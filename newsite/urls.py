from django.conf.urls import patterns, include, url
from login.views import *
 
urlpatterns = [
        #the ones related to the login app
	url(r'^$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', logout_page),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
	url(r'^register/$', register),
	url(r'^register/success/$', register_success),
	url(r'^home/$', home),
	url('r^$', 'newsite.login.views.index'),
	url(r'^todo/add/$', add),
	url('r^$', 'newsite.login.views.add'),
	url(r'^delete/delete/$', delete),
	url(r'^$', 'newsite.login.views.delete'),
	url(r'^$', 'newsite.login.views.edit'),
	url(r'edit/$', edit),
]