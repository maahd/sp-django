# Urls and HttpResponses
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, render_to_response

# User forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Permission
from meddy1.forms import *
from django.utils.html import escape

# Authentication and Users
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.context_processors import csrf
from django.template import RequestContext

# Models
from meddy1.models import *

# Mailer
from django.core.mail import send_mail

# Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Other Imports
import random
from django.conf.urls import patterns, url


# Image Handlers
from base64 import b64decode
from django.core.files.base import ContentFile

def index(request):
    return render(request, 'meddy1/index.html')



 # def showSeekerProfile(request):
 #    profile = request.user.get_profile()
 #    return render(request,'meddy1/profile.html', d)



# -------------------- Authentication ----------------------
def signup(request):
    return render(request, 'meddy1/signup.html', {})

@csrf_exempt
def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=request.POST['username'],password=request.POST['password1'])
            login(request, new_user)
            
            return HttpResponseRedirect(reverse('index'))
    else:
        form = UserCreationForm()
    return render(request, "meddy1/signup.html", {'form': form,'usersignup':True})



def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user:
        return render(request, 'meddy1/index.html')
    else:
        return HttpResponseRedirect('/')

        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
