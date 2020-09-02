"""
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

# import the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# data reader function
def city_get_data(a=None):
	# check for the default case
	if a is None:
		# extract the longitute list 
		x = np.array(city_get_data.df.Longitude)
		# extract the latitude lists
		y = np.array(city_get_data.df.Latitude)
		# extract the city names 
		city = np.array(city_get_data.df.City)
		# extract the distance matrix
		D = np.array(city_get_data.df.iloc[:,4:])
		# return the data elements
		return x, y, city, D
	else:
		# initialize the persistent variable
		city_get_data.df = pd.read_csv('city_data.csv')
		return

# plot the entire map
def city_data_plot(cities=True, distances=False, ax=None):
	# check for the default axis
	if ax is None: ax = plt.gca()
	# define the color of the connection lines
	colspec = 0.8*np.array([1.0,1.0,1.0])
	# get the data elements
	x, y, city, D = city_get_data()
	# get the number of cities
	N = city.shape[0]
	# plot all of the connection lines
	for r in range(N):
		for c in range(r+1,N):
			if D[r,c] > 0:
				# extrct the component values
				x1 = x[r]; y1 = y[r]; x2 = x[c]; y2 = y[c]
				# plot the connection lines
				ax.plot([x1,x2],[y1,y2],c=colspec,linestyle='-',zorder=-2)
				# check if distance numbers are required
				if distances is True:
					# plot the distance numbers
					ax.text((x1+x2)/2,(y1+y2)/2,str(int(D[r,c])),
						va='center',ha='center',size='small')
	# plot the city location marker 
	ax.scatter(x, y, c='b', marker='o', alpha=1.0, s=20)
	# plot all of the city names
	if cities is True:
		for i in range(N):
			ax.text(x[i],y[i],' ' + city[i],va='center',size='small')
	# label the axis 
	ax.set_xlabel('Longitude') #,size='small')
	ax.set_ylabel('Latitude') #,size='small')
	ax.set_title('US Cities Map')
	# format the tick marks
	ax.tick_params(labelsize='small')
	xfmt = plt.FixedLocator(np.arange(-125,-60,5))
	ax.xaxis.set_major_locator(xfmt)
	yfmt = plt.FixedLocator(np.arange(25,55,5))
	ax.yaxis.set_major_locator(yfmt)
	# control the axis limits
	ax.set_xlim((-126,-62))
	ax.set_ylim((24,51))
	# set grid lines below the map
	ax.grid(True,linestyle=':')
	ax.set_axisbelow(True)

# find city name indices
def city_index(names,city_list=None):
	# check for the default list of city names
	if city_list is None:
		# extract the city list
		x, y, city_list, D = city_get_data()
	# check for the names and convert to list
	if isinstance(names, str): names = [ names ]
	# make sure the names list is an numpy array
	names = np.array(names)
	# make sure the city-list is an array
	if not isinstance(city_list,np.ndarray): city_list = np.array(city_list)
	# initialize the index vector
	i = [ -1 for i in range(names.shape[0]) ]
	# scan through all names
	for k in range(names.shape[0]):
		# find the indices of names in the list
		m = (city_list == names[k]).nonzero()[0]
		# skip if no name was found
		if len(m) > 0: i[k] = int(m[0])
	# return the index list
	return i

# find the neighbors of a city
def city_neighbors(name):
	# check the city name index
	i = city_index(name)[0]
	# check if city does not exist
	if i < 0: return [], []
	# extract the city information
	x, y, city, D = city_get_data()
	# extract the neighbor indices
	dd = D[i].nonzero()[0];
	# extract the distances
	d = D[i,dd]
	# extract the city names
	n = city[dd]
	# return the answer
	return list(n), list(d)

# plot a particular path
def city_path_plot(city_list, ax=None):
	# check for the default axis
	if ax is None: ax = plt.gca()
	# extract the city information
	x, y, city, D = city_get_data()
	# get the indices into the city list
	i = city_index(city_list)
	# generate a line color scheme
	c = [ 'g' for k in range(len(i)-1) ]
	# generate a line style scheme
	s = [ '-' for k in range(len(i)-1) ]
	# scan through all names in the list
	for k in range(len(city_list)-1):
		# find all neighbors
		names, d = city_neighbors(city_list[k])
		# check for connection membership
		if city_list[k+1] not in names: c[k] = 'r'; s[k] = '--'
	# execute the line drawing
	for k in range(len(c)):
		# define the color and line style
		cc = c[k]; ss = s[k]
		# define the start and end indices
		si = i[k]; ei = i[k+1]
		# check that both indices are valid
		if (si >= 0) and (ei >= 0):
			# plot the line segment
			ax.plot([x[si],x[ei]],[y[si],y[ei]],c=cc,linestyle=ss,
				linewidth=3, zorder=-1)
	# finish the function
	return

# initialize the data reader function
city_get_data('init')
