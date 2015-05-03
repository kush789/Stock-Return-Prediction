from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from index.models import *
import os

def index(request):
	return render_to_response('index.html')
