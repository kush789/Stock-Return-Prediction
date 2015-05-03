from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from index.models import *
import os
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'DOWJONES.csv')

def index(request):
	# g = open(file_path, "r")
	# num = 0
	# a = g.readlines()[1:][::-1]

	# for i in range(len(a)):
	# 	a[i] = a[i].strip("\n")
	# 	a[i] = a[i].split(",")
	# 	sample = DOWJONES(dowjonesid = num, value = float(a[i][1]), date = a[i][0])
	# 	sample.save()
	# 	num += 1
	# 	print num
	# # g.close()	
	# for i in DOWJONES.objects.all():
	# 	print i.dowjonesid, i.value, i.date
	return render_to_response('index.html')
