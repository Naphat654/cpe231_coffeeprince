from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm

def registerPage(request):
	
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)

			return render(request,'home/Home.html')
			

	context = {'form':form}
	return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return render(request,'home/Home.html')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return render(request,'home/Home.html')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	#return redirect('login')
	return render(request,'home/Home.html')


@login_required(login_url='login')
def home(request):
    return render(request,'home/Home.html')