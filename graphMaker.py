import networkx as nx
from networkx.algorithms.flow import edmonds_karp
import matplotlib.pyplot as plt
from constants import *
import pandas as pd
from helper import *

''' Creates the graph that we will run max flow on 
'''
def create_graph(bros, tasks, brocapacity, preferences):
	# Initialize Graph
	G = nx.DiGraph()

	# Add source and sink nodes
	G.add_node('source')
	G.add_node('sink')

	# Add bro nodes and bro->bro nodes
	G.add_nodes_from(bros)
	updated_bros = [bro + '_2' for bro in bros]
	G.add_nodes_from(updated_bros)

	# Add task nodes
	G.add_nodes_from(tasks)

	# Add edge from source to bros
	G.add_edges_from([('source', bro) for bro in bros])

	# Add edge from bro to bros with capacity from brocapacity
	for bro in bros:
		v1 = bro
		v2 = bro + '_2'
		capacity = brocapacity[bro]
		G.add_edge(v1, v2, capacity = capacity)

	# Add edge from bro to tasks with capacity from preferences
	for edge, value in preferences.items():
		v1, v2 = edge
		v1 += '_2'
		G.add_edge(v1, v2, capacity = value)

	# Add edge from task to sink with capacity 1
	for task in tasks:
		G.add_edge(task, 'sink', capacity = 1.0)
	return G

''' Given a graph, computes the max flow from source to sink
using Edmonds-Karp algorithm
'''
def run_flow(graph, source = 'source', sink = 'sink'):
	R = edmonds_karp(graph, source, sink, capacity = 'capacity')
	return R

''' Turn residual graph into actual midnight assignments '''
def residual_to_midnights(R, bros, tasks = all_tasks, days_map = days_map, heavy_bathrooms = heavy_bathrooms):
	flow = list(R.edges_iter(data='flow'))
	bros = set(bros)
	tasks = set(tasks)
	midnights = []
	for edge in flow:
		v1 = edge[0]
		v2 = edge[1]
		value = edge[2]
		if (v1[:-2] in bros) and (v2 in tasks) and (value == 1.0):
			curr_dict = {}
			curr_task = v2[:-1]
			if curr_task[-1] == '1' or curr_task[-1] == '2':
				curr_task = curr_task[:-1]		

			# Check if bathrooms is a heavy bathrooms day, if so, change the name to 'Heavy Bathrooms'
			if curr_task == 'Bathrooms' and int(v2[-1]) in heavy_bathrooms:
				curr_task = 'Heavy Bathrooms'

			curr_day = days_map[v2[-1]]
			curr_day = get_next_weekday(curr_day)
			curr_dict = {'zebe': v1[:-2], 'date': curr_day, 'task': curr_task}
			midnights.append(curr_dict)
	return midnights