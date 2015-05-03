from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from index.models import *
import os

module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'NIKKEI.csv')

def index(request):
	return render_to_response('index.html')
