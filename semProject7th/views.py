from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth import authenticate, login
#from django.views.generic import views
from django.template import loader
from django.views import generic
#from django.core.urlresolver import reverse_lazy
from django.contrib import auth
from django.core.context_processors import csrf




