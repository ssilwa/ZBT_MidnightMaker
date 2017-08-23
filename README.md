## Introduction

This is the updated midnight maker script for ZBT Fraternity at MIT. 


## Installation

See the directions here: https://help.github.com/articles/cloning-a-repository/

## How to Use

CD into the directory you created from the step above. Make sure you have Python3 installed in your machine. Open a terminal and type 

```python
python3 midnightmaker.py
```

This will automatically pull the current data about preferences and points
and output this week's assignments (once we have the website running).
If there are any errors, make sure you have all the packages from the requirements.txt file installed. All of them should be installable using pip3. 

## Quick Overview of the Algorithm

There are three main parts to the midnight assigning algorithm.

### Specification

Every brother gets to specify two things:

1) The chores they would like to do and not like to do
2) The days they would like to work and not like to work

```
Note: a midnight is defined by a chore AND a day
```

### Bucketing

Brothers are bucketed into four quartiles based on their current midnight points.
Quartle 1 bros have the most points and quartile 4 bros have the least points.
Since quartile 1 bros have a lot of points, they should not be doing a lot of midnights
and similarly, quartile 4 bros should be doing most of the midnights. Currently, the number of midnights per week is 54. The breakdown of midnights allocated to each quartile is: Quartile 1: 7, Quartile 2: 10, Quartile 3: 16, Quartile 4: 21
(roughly 10%, 20%, 30%, 40%).

### Matching 

Given the specification and bucketing constraints above, we try to determine if 
if all the midnights throught the week can be done (a valid assignment). This is done by creating a graph that encodes the constraints above and reformulating the problem as a maximum flow problem (details about this in the section below). If a valid assignemnt is possible, we are done. Otherwise, we take away the specification constraints of the quartile 4 brothers and try agian. If we are done, great; otherwise, we take away the specifications of the quartile 3 brothers and try again, etc. If there are no specifications for all the brothers, we are guarenteed to find a valid assignment (see section below). 

## Detailed Overview of the Algorithm

### Graph construction

Suppose we have N bros that do midnights and M midnights this week. As stated above, the M midnights are actually tuples of the form (chore, day) where chores is either bathrooms, or kitchens or, etc and day is either Sunday, or Monday, etc. We represent each bro and midnight as a vertex. We also add a source and a target vertex. We connect each of the bro vertices to the source vertex with an edge of capacity infinity. We also connect each midnight vertex to the target vertex with an edge of capacity 1.

<p align="center">
<img src="Images\graph_img1.png" width="600">
</p>



### Encoding Specification Constraints

We also add an edge between every brother and every midnight. If brother b_i wants to do midnight m_j (based on both the chore and day), then the edge (b_i, m_j) will have capacity 1. Otherwise, this edge will have capacity 0. 

<p align="center">
<img src="Images\graph_img2.png" width="600">
</p>

### Encoding Bucketing Constraints

To deal with the bucketing constraints as described above, we need to add a constraint for each bro vertex. For each of the four quartiles, we fairly distribute the number of midnights assigned to that quartile among each of the bros in that quatile (some bros might have one more midnights than others in the same quartile due to rounding). To encode this into our graph, we replace each bro vertex (say b_i) with two vertices (b_i and b_i') and add an edge between them. We let the capacity of that edge be c_i, the number of midnights assigned to that bro. Intuitively, this number represents the maximum number of midnights bro b_i is allowed to do this week. Due to how we allocate the total number of midnights among quartiles, bros in quartile 1 will have a lower maximum than bros in quartile 4.

<p align="center">
<img src="Images\graph_img3.png" width="600">
</p>

### Max Flow 

We finally run a max flow algorithm in the graph created above from the source vertex to the target vertex. The algorithm used is Edmonds-Karp. The positive flow in the residual graph gives us our midnight assignments. (Quick note: since each edge capacity is a positive integer, we are guarenteed to find an integral flow.) If all of the edges between bros and tasks have weight 1, it is easy to see that the min cut is between the tmidnight vertices and the target vertex. Therefore, our program is guarenteed to find an assignment (some bros might lose their specification constraints as described above).











