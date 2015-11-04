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
	url(r'^add/$', add),
	url('r^$todo', 'newsite.login.views.add'),
]