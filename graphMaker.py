import networkx as nx
from networkx.algorithms.flow import edmonds_karp
import matplotlib.pyplot as plt
from constants import *
import pandas as pd

''' Creates the graph that we will run max flow on 
'''
def create_graph(bros, tasks, brocapacity, preferences):
	# Initialize Graph
	G = nx.Graph()

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
	R = edmonds_karp(graph, source, sink)
	return R

''' Turn residual graph into actual midnight assignments '''
def residual_to_midnights(R, bros, tasks = all_tasks, days_map = days_map):
	flow = list(R.edges_iter(data='flow'))
	bros = set(bros)
	tasks = set(tasks)
	midnights = {}
	for edge in flow:
		curr_dict = {}
		v1 = edge[0]
		v2 = edge[1]
		value = edge[2]
		if v1[:-2] in bros and v2 in tasks and value > 0:
			curr_task = v2[:-1]
			curr_day = days_map[v2[-1]]
			midnights[(curr_task, curr_day)] = v1[:-2]
	return midnights