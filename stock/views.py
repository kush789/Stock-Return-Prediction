from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
import json
from artificial_neural_network import *
from index.models import *
from stock.models import *

import os

module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'WIKI-MSFT.csv')

def modd(x):
	if x < 0:
		return -1 * x
	else:
		return x

def index(request):
	return render_to_response('stock.html')

def msft(request):
	# g = open(file_path, "r")
	# k = 0


	# values = g.readlines()[1:]
	# for i in range(len(values)):
	# 	values[i] = values[i].strip("\n")
	# 	values[i] = values[i].split(",")

	# for i in values:
	# 	k += 1
	# 	sample = MSFT(msftid = k, date = i[0], value = float(i[1]))
	# 	sample.save()
	# 	print k



	return render_to_response('msft.html')

def msft_update(request, param):
	input_weights = []
	hidden_weights = []

	if request.is_ajax():

		for i in range(10):
			temp = []
			for j in request.POST.getlist("input[" + str(i) + "][]"):
				temp.append(float(j))
			input_weights.append(temp)

		for i in range(15):
			temp = []
			for j in request.POST.getlist("hidden[" + str(i) + "][]"):
				temp.append(float(j))
			hidden_weights.append(temp)

	input_data = []
	output_data = []
	predicted_data = []

	param = int(param)
	param += 2000
	for i in range(int(param), int(param) + 10):
		input_data.append(MSFT.objects.get(msftid = i).value)

	for i in range(int(param) + 10, int(param) + 13):
		output_data.append(MSFT.objects.get(msftid = i).value)

	in_t_min_one = float(input_data[-1])

	hidden_bias =  [-0.282131747887 ,-0.37632723384 ,-0.201913460002 ,
					0.462031787676 ,0.158895292575 ,-0.247847691534 ,
					-0.195471918314 ,-0.118778832854 ,0.306206070501 ,
					-0.484578529401 ,0.121857280681 ,0.355322548494 ,
					-0.477332292337 ,-0.0553123901142 ,0.184024330442]

	output_bias = [0.418767336723, 0.458851246215, 0.454579349485]

	max_data = 178.94 
	min_data = 25.5
	den = 153.44

	network = neural_network(0.5, 0.001)
	network.set_input_layer(10, input_weights)
	network.set_hidden_layer(15, hidden_weights, hidden_bias)
	network.set_output_layer(3, output_bias)


	for i in range(len(input_data)):
		input_data[i] = ((input_data[i] - min_data) / den) * 0.8 + 0.1

	for i in range(len(output_data)):
		output_data[i] = ((output_data[i] - min_data) / den) * 0.8 + 0.1

	network.learn(input_data, output_data)

	for i in range(3):
		predicted_data.append(network.output_layer.nodes[i].output_value)

	for i in range(len(output_data)):
		output_data[i] = ((output_data[i] - 0.1) / 0.8) * den + min_data

	for i in range(len(predicted_data)):
		predicted_data[i] = ((predicted_data[i] - 0.1) / 0.8) * den + min_data

	for i in range(network.input_layer.total):
		for j in range(network.hidden_layer.total):
			input_weights[i][j] = network.input_layer.nodes[i].weight[j]

	for i in range(network.hidden_layer.total):
		for j in range(network.output_layer.total):
			hidden_weights[i][j] = network.hidden_layer.nodes[i].weight[j]

	data = {}
	data['input_layer'] = input_weights
	data['hidden_layer'] = hidden_weights
	data["prev"] = "{0:.2f}".format(in_t_min_one)
	data["pred"] = "{0:.2f}".format(predicted_data[0])
	data["right"] = "{0:.2f}".format(output_data[0])

	if modd(predicted_data[0] - output_data[0]) > 5:
		network.set_learning_rate(0.5)
	elif modd(predicted_data[0] - output_data[0]) > 1:
		network.set_learning_rate(0.3)

	if modd(predicted_data[0] - output_data[0]) < 0.5:
		network.set_mobility_factor(0.0001)
		network.set_learning_rate(0.1)
	else:
		network.set_mobility_factor(0.001)
	return HttpResponse(json.dumps(data), content_type="application/json")	


