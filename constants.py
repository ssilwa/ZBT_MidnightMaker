''' Constants that can be configured.
Basically the only file that you should change.
'''

###################### Editable Start ######################

################ Tasks ################
# 0 = sunday, 1 = Mon, ..., 5 = sat
# Bath1, Bath2 = Two bathroom midnights
# Wait1, Wait2 = Two waitings midnights
task_labels = ['Bathrooms', 'Cluster', 'Commons', 'Dinings', 'Dishes', 'Kitchens', 'Waitings']
tasks_dict = {'Bathrooms1': [0,1,2,3,4,5], 'Bathrooms2': [1,4], \
          'Cluster': [0,1,2,3,4,5], \
          'Commons': [0,1,2,3,4,5], \
          'Dinings': [0,1,2,3,4,5], \
          'Dishes': [0,1,2,3,4,5], \
          'Kitchens1': [0,1,2,3,4,5], 'Kitchens2': [0,1,2,3,4,5], \
          'Waitings1': [0,1,2,3,4], 'Waitings2': [0,1,2,3,4]}

################ Task allocation among quartiles ################

# The total number of tasks is 54 currently
# Allocation is roughly 40%, 30%, 20%, 10%

quartile_1_tasks = 6
quartile_2_tasks = 11
quartile_3_tasks = 16
quartile_4_tasks = 21

###################### Editable End ######################

all_tasks = [task + str(day) for task, days in tasks_dict.items() for day in days]
num_tasks = len(all_tasks)
days_map = {'0': 'Sunday', '1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Friday', '6': 'Saturday'}