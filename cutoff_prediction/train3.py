from node import node
from layer import layer
from network import network
import math
import numpy as np


#initialising network parameters
batch_size=5 			#number of year (each year will give one example)
regularisation=2500
descent_rate=0.000008

#creating network graph
input_layer=layer('input',[(1,1,'biased'),(1,2,'un_biased')],batch_size)
output_layer=layer('output',[(1,1,'un_biased')],batch_size)

#initializing the network
input_layer.initialize_layer()
output_layer.initialize_layer()

input_layer.create_connection(output_layer,[('one_to_all',),('one_to_all',)])
all_layer_list=[input_layer,output_layer]

net=network(all_layer_list,'stochastic',batch_size,regularisation,descent_rate)


temp=0
while temp<50:
	list_of_input=[(),(302,296)]
	list_of_output=[(294,)]
	net.in_batch_initialize_network()
	net.initialize_input_output_layer(list_of_input,list_of_output)
	net.network_foreward_propagate()
	net.network_back_propagate()
	print output_layer.sub_units[0][0][0].a_val,output_layer.sub_units[0][0][0].Y
	
	
	list_of_input=[(),(294,302)]
	list_of_output=[(307,)]
	net.in_batch_initialize_network()
	net.initialize_input_output_layer(list_of_input,list_of_output)
	net.network_foreward_propagate()
	net.network_back_propagate()
	print output_layer.sub_units[0][0][0].a_val,output_layer.sub_units[0][0][0].Y

	list_of_input=[(),(307,294)]
	list_of_output=[(316,)]
	net.in_batch_initialize_network()
	net.initialize_input_output_layer(list_of_input,list_of_output)
	net.network_foreward_propagate()
	net.network_back_propagate()
	print output_layer.sub_units[0][0][0].a_val,output_layer.sub_units[0][0][0].Y

	list_of_input=[(),(316,307)]
	list_of_output=[(329,)]
	net.in_batch_initialize_network()
	net.initialize_input_output_layer(list_of_input,list_of_output)
	net.network_foreward_propagate()
	net.network_back_propagate()
	print output_layer.sub_units[0][0][0].a_val,output_layer.sub_units[0][0][0].Y


	list_of_input=[(),(329,316)]
	list_of_output=[(339,)]
	net.in_batch_initialize_network()
	net.initialize_input_output_layer(list_of_input,list_of_output)
	net.network_foreward_propagate()
	net.network_back_propagate()
	print output_layer.sub_units[0][0][0].a_val,output_layer.sub_units[0][0][0].Y


	output_layer.cost_calculation('squared')
	print 'Cost_Incurred: ',output_layer.cost_incurred
	net.start_gradient_descent()
	net.batch_initialize_network()


	temp+=1
	print ""



