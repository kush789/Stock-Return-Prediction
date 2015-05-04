from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
import json
from artificial_neural_network import *
from index.models import *

def modd(x):
	if x < 0:
		return -1 * x
	else:
		return x
		
def index(request):
	return render_to_response('marketindex.html')

def nasdaq(request):
	return render_to_response('NASDAQ.html')

def nasdaq_update(request, param):

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
	param += 2500
	for i in range(int(param), int(param) + 10):
		input_data.append(NASDAQ.objects.get(nasdaqid = i).value)

	for i in range(int(param) + 10, int(param) + 13):
		output_data.append(NASDAQ.objects.get(nasdaqid = i).value)

	in_t_min_one = float(input_data[-1])

	hidden_bias = [ -0.281728223377, 0.48815158608, 0.205840354146, 
				    -0.279562975759, -0.247434371695, -0.241613701801,
				     0.36534473384, -0.0378311044, 0.0948569991864,
				    -0.437962844979, 0.3300770123, -0.201334661889, 
				    -0.432786357923, 0.176590042923, -0.185177510502 ]

	output_bias = [0.314226920406, 0.0832572815584, 0.278136194639]

	max_data = 5092.08 
	min_data = 1261.79 
	den = 3830.29

	network = neural_network(0.5, 0.0001)
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

	if modd(predicted_data[0] - output_data[0]) > 100:
		network.set_learning_rate(0.5)
	else:
		network.set_learning_rate(0.3)

	return HttpResponse(json.dumps(data), content_type="application/json")	
