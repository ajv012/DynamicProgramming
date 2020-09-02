"""
This Python script demonstrates how to
use the functions provided by the city_data
module.

The data used in this module was taken from:
<https://simplemaps.com/data/us-cities>
"""
# =====================================
# (C) Copyright, 2020, Robert M. Nickel
# =====================================
# This contents of this file may not be shared without permission.

"""
This work was done for Prof. Robert Nickel ECEG 403 class
"""

# import the required modules
import matplotlib.pyplot as plt
import city_data as cd

# a plot of the complete map with all
# considered cities can be generated with
fig = plt.figure(figsize=[9,6])
ax = plt.subplot(111)
cd.city_data_plot(cities=True,distances=False)
# displaying of the city names and/or the
# distances between them in miles can be
# selected with the respective True/False
# assignments

# # a particular path from city to city to city can be
# # highlighted with a thick green line in the map with
# PATH = ['Reno','Provo','Colorado Springs','Wichita','Lubbock']
# cd.city_path_plot(PATH)

# # note that any path segment that does not represent
# # a valid connection is drawn as a red dashed line
# PATH = ['Fargo','Lincoln','St. Louis','Nashville','Atlanta']
# cd.city_path_plot(PATH)

# # one can query a list of all neighboring cities of a
# # given city, including the associated distances, with
# CITY = 'Augusta'
# NEIGHBORS, DISTANCES = cd.city_neighbors(CITY)
# print("The neighboring cities of '" + CITY + "' are:")
# print(NEIGHBORS)
# print('with the respective distances in miles:')
# print(DISTANCES)

# # for your programmming assignment you may also find the
# # following procedure useful which extracts the index i
# # of a city in a list of cities
# CITY = 'Greenville'
# i = cd.city_index(CITY,city_list=NEIGHBORS)
# # variable i always contains a list of indices; it is a list
# # with a single entry if we are only searching for a single city
# print("City '" + CITY + "' is at index " + str(int(i[0])) + " in the list:")
# print(NEIGHBORS)
# # note that the CITY variable in the above example may also
# # be a list of cities in which case variable i contains a
# # list of the associated indices; the index -1 is returned
# # for city names that cannot be found

# execute the display event queue
plt.show()