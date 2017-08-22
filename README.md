### Introduction

This is the updated midnight maker script for ZBT Fraternity at MIT.


### Installation

See the directions here: https://help.github.com/articles/cloning-a-repository/

### How to Use



### Overview of the Algorithm

There are three main parts to the midnight assigning algorithm.

# Specification

Every brother gets to specify two things:

1) The tasks they would like to do
2) The days they would like to work

# Bucketing

Brothers are bucketed into four quartiles based on their current midnight points.
Quartle 1 has the most points and quartile 4 has the least points.
Since quartile 1 bros have a lot of points, they should not be doing a lot of midnights
and similarly, quartile 4 bros should be doing most of the midnights. Currently, the number of tasks per week is 54. The breakdown of tasks allocated to each quartile is:

quartile 1: 7
quartile 2: 10
quartile 3: 16
quartile 4: 21

(roughly 10%, 20%, 30%, 40%).



