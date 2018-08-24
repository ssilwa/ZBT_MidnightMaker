''' Constants that can be configured.
Basically the only file that you should change.
'''
import math

###################### Editable Start ######################

################ Tasks ################
# 0 = sunday, 1 = Mon, 2 = Tue, 3 = Wed, 4 = Thurs, 5 = sat
# Bath1, Bath2 = Two bathroom midnights
# Wait1, Wait2 = Two waitings midnights
task_labels = ['Bathrooms', 'Cluster', 'Commons', 'Dinings', 'Dishes', 'Kitchens', 'Waitings']
# Do heavy bathrooms on days 1 and 4 (Monday and Thursday)
tasks_dict = {'Bathrooms1': [0,1,2,3,4,5], 'Bathrooms2': [1,4], \
          'Cluster': [0,1,2,3,4,5], \
          'Commons': [0,1,2,3,4,5], \
          'Dinings': [0,1,2,3,4,5], \
          'Dishes': [0,1,2,3,4,5], \
          'Kitchens1': [0,1,2,3,4,5], 'Kitchens2': [0,1,2,3,4,5], \
          'Waitings1': [0,1,2,3,4], 'Waitings2': [0,1,2,3,4]}

# Heavy bathrooms on these days only
heavy_bathrooms = [1,4]

# Percentage of midnights given to the quartiles
quartile_2_perct = .2
quartile_3_perct = .3
quartile_4_perct = .4


# Bros that are exempt from midnights, update this as the semester goes on
exempt_bros = ['silwal']

###################### Editable End ######################

exempt_bros = set(exempt_bros)
all_tasks = [task + str(day) for task, days in tasks_dict.items() for day in days]
num_tasks = len(all_tasks)
days_map = {'0': 'Sunday', '1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday', '5': 'Saturday'}

################ Task allocation among quartiles ################

# The total number of tasks is 54 currently
# Allocation is roughly 40%, 30%, 20%, 10%

quartile_4_tasks = math.floor(num_tasks*quartile_4_perct)
quartile_3_tasks = math.floor(num_tasks*quartile_3_perct)
quartile_2_tasks = math.floor(num_tasks*quartile_2_perct)
quartile_1_tasks = max(0, num_tasks - quartile_2_tasks - quartile_3_tasks - quartile_4_tasks)


