from constants import *
import numpy as np
import random
import pandas as pd

''' Helper script for midnightmaker.py
'''

''' Get current points for every bro
Output format: [(bro1, points1), (bro2, points2), ...]
'''
def get_current_points():
	currpoints = pd.read_excel('test_points.xlsx')
	return list(zip(currpoints.Brother, currpoints.Points))

''' Get days and task preferences for every bro.
Day preference output format: {bro1: {'Monday': 0, 'Tuesday': 1, etc}, etc}
Task preference output format: {bro1: {'Kitchens': 1, 'Bathrooms': 0, etc}, etc}
'''
def get_current_preferences(tasks = task_labels):
	currprefs = pd.read_excel('test_preferences.xlsx')
	days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	prefs_days = currprefs[['Brother'] + days]
	prefs_days.index = prefs_days['Brother']
	prefs_days = prefs_days[days]
	prefs_days_dict = prefs_days.to_dict(orient = 'index')
	prefs_tasks = currprefs[['Brother'] + tasks]
	prefs_tasks.index = prefs_tasks['Brother']
	prefs_tasks = prefs_tasks[tasks]
	prefs_tasks_dict = prefs_tasks.to_dict(orient = 'index')
	return (prefs_days_dict, prefs_tasks_dict)

# Helper function for make_bro_capacity
def allocate_tasks(num_tasks, bros):
	capacity = {}
	try:
		rounded_capacity = np.floor(num_tasks/len(bros))
		for bro in bros:
			capacity[bro] = rounded_capacity
		diff = num_tasks - rounded_capacity*len(bros)
		curr_index = 0
		while diff != 0:
			curr_bro = bros[curr_index]
			capacity[curr_bro] += 1
			curr_index += 1
			diff -= 1
		return capacity
	except:
		return None

'''
Function to allcoate tasks among bros based on percentile.
Returns a dict with key value pairs:
key: bro
value: max number of tasks that he can do this week
'''
def make_bro_capacity():
	bro_points = get_current_points()
	bro_points.sort(key = lambda x: x[1])
	curr_points = [ _[1] for _ in bro_points]

	# Find percentiles
	top25 = np.percentile(curr_points, 75)
	top50 = np.percentile(curr_points, 50)
	top75 = np.percentile(curr_points, 25)

	# Break bros into percentiles
	quartile_1_bros = [bro[0] for bro in bro_points if bro[1] >= top25]
	quartile_2_bros = [bro[0] for bro in bro_points if top25 > bro[1] >= top50]
	quartile_3_bros = [bro[0] for bro in bro_points if top50 > bro[1] >= top75]
	quartile_4_bros = [bro[0] for bro in bro_points if bro[1] < top75]

	# Get capacity of bros based on percentiles
	capacity = {}
	all_quartiles = [(quartile_1_bros, quartile_1_tasks), (quartile_2_bros, quartile_2_tasks), (quartile_3_bros, quartile_3_tasks), (quartile_4_bros, quartile_4_tasks)]
	for quartile in all_quartiles:
		try:
			curr_capacity = allocate_tasks(quartile[1], quartile[0])
			capacity.update(curr_capacity)
		except:
			pass
	return (quartile_1_bros, quartile_2_bros, quartile_3_bros, quartile_4_bros, capacity)


''' Return dictionary with:
key: (bro, task)
value: 1 if bro wants to do it, 0 otherwise.
If bro A doesn't like task X, then capacity of that edge is ideally 0
'''
def make_task_capacity(all_tasks = all_tasks, days_map = days_map):
	days_prefs, tasks_prefs = get_current_preferences()
	task_capacity = {}
	bros = list(days_prefs.keys())
	for bro in bros:
		for task in all_tasks:
			currday = task[-1]
			currday = days_map[currday]
			currtask = task[:-1]
			currtask = ''.join(filter(lambda x: x.isalpha(), currtask))
			if days_prefs[bro][currday] == 1 and tasks_prefs[bro][currtask] == 1:
				task_capacity[(bro, task)] = 1.0
			else:
				task_capacity[(bro, task)] = 0.0
	return task_capacity