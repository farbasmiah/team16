from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django import forms
from . import models
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
	username = request.user.username
	todo = models.todo.objects.all()
	#todo = models.todo.objects.filter(models.todo.name.username = username).order_by('id')
	return render_to_response(
	'home.html',
	{ 'user': request.user,
	'todo' : todo}
	)

def index(request):
	items = newsite.objects.User.all()
	return render_to_response('home.html', {'items': items})
	
def add(request):
	if request.method == 'POST':
		form = ToDoForm(request.POST)
		if form.is_valid():
			obj = models.todo.objects.create(
			#name = form.cleaned_data['name'],
			description = form.cleaned_data['description']
			)
			#created = form.cleaned_data['created']
			return HttpResponseRedirect('/home/')
	else:
		form = ToDoForm()
	variables = RequestContext(request, {
	'form': form
	})
	
	return render_to_response(
	'todo/todo.html',
	variables,
	)	