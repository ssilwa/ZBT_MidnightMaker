from graphMaker import *
from helper import *
from constants import *
from emailer import *
import datetime
import time
import requests
import json

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

	# Turn max flow into assignments
	curr_assignments = residual_to_midnights(Residiual, bros)
	print(len(curr_assignments))
	return curr_assignments
 
''' Emails ppl about their assignments. Might not work in the future if Google
changes its security settings so beaware.'''  
def emailer(curr_assignments, fromaddr = 'mitzbtmidnightmaker', password = 'Br0therhood'):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, password)
	for midnight in curr_assignments:
		date = midnight['date']
		task = midnight['task']
		kerberos = midnight['zebe']
		toaddr = "silwal@mit.edu"
		# toaddr = kerberos + '@mit.edu'
		subject = '[Midnights] You have ' + task + ' on ' + date + ' eom.'
		body = ''
		send_email(server, toaddr, subject, body)
	server.quit()





if __name__ == '__main__':
	start = time.time()
	print("Getting points and preferences")
	curr_assignments = main()
	print("Assigned Midnights")
	print(curr_assignments)
	# midnights = {'midnights': curr_assignments}
	print("Sending Assignments to ZBTodo")
	# secret_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXJiZXJvcyI6InNpbHdhbCIsImlhdCI6MTUwODYzMjE3NDg1OCwiZXhwIjoxNTA4NjMzOTc0ODU4fQ.XHR2RIVrjKPvWkD7RKzafqXbEmPdbqsqquwV-P7RcOA"
	# r = requests.post('https://zbt-backend.herokuapp.com/api/v1/midnights/bulk_create', headers = {'Authorization': secret_token}, json = midnights)
	# print(r.status_code)
	print("Emailing Assignments")
	# emailer(curr_assignments)
	print("Total Time Taken:")
	print(time.time() - start)
