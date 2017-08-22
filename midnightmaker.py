from graphMaker import *
from helper import *
from constants import *
import datetime
from collections import Counter
import time

''' Main function for assigning midnights
'''
def main():
	# TODO Get data from website

	# Compute capacity and preferences
	quartile_1_bros, quartile_2_bros, quartile_3_bros, quartile_4_bros, brocapacity = make_bro_capacity()
	preferences = make_task_capacity()
	bros = list(brocapacity.keys())
	tasks = all_tasks

	# Make graph
	Graph = create_graph(bros, tasks, brocapacity, preferences)

	# Compute max flow
	Residiual = run_flow(Graph)

	# TODO Check if max flow is satisfiable
	quartile_bros = {1: quartile_1_bros, 2: quartile_2_bros, 3: quartile_3_bros, 4: quartile_4_bros}
	curr_to_revoke = 4
	while num_tasks != Residiual.graph['flow_value']:
		bros_to_revoke = quartile_bros[curr_to_revoke]
		for bro in bros_to_revoke:
			for key in preferences:
				if key[0] == bro:
					preferences[key] = 1.0
		curr_to_revoke -= 1
		Graph = create_graph(bros, tasks, brocapacity, preferences)
		Residiual = run_flow(Graph)
		print('here')
		print(Residiual.graph['flow_value'])

	# Turn max flow into assignments
	curr_assignments = residual_to_midnights(Residiual, bros)

	# Frequency counts:
	frequency = curr_assignments.values()
	counts = Counter(frequency)
	print(counts)
	# print(curr_assignments)

	# TODO Put assignments in website

	return curr_assignments

if __name__ == '__main__':
	start = time.time()
	main()
	print(time.time() - start)