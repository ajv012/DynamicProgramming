"""
The data used in this module was taken from:
<https://simplemaps.com/data/us-cities>
"""

"""
This work was done for Prof. Robert Nickel ECEG 403 class
"""

# import the required modules
import matplotlib.pyplot as plt
import city_data as cd


# dynamic programming routine to find the best path
def best_city_path(OrigCity,DestCity):
    # REPLACE THE CODE BELOW:
    # =======================
    # create a dummy path
    PATH = []
    # and a dummy distance
    DIST = 0
    # =======================
    # return the path and distance
    
    # initialize the columns of dynamic programming algorithm
    nodes = [OrigCity]
    check = [True]
    bestCumCost = [0]
    bestPred = [""]
    
    # manually perform first iteration of dynamic programming
    # for first entry, find all neighbours
    NEIGHBORS, DISTANCES = cd.city_neighbors(OrigCity)
    
    # find cum cost for each neighbour
    index = cd.city_index(OrigCity,city_list=nodes)[0]
    for i in range(len(NEIGHBORS)):
        nodes.append(NEIGHBORS[i])
        bestCumCost.append(bestCumCost[index] + DISTANCES[i])
        bestPred.append(OrigCity)
        check.append(False) 
    
    # now you have the first iteration done
    continueBigLoop = True
    while continueBigLoop:
        
        # set up a variable to check if we need to start from the beginning
        startFromBegin = False
        
        # iterate over check list
        for i in range(len(check)):
            
            # if a check is false then do the table algo and set that check to true
            if not check[i]:
                # this city is not checked, so do table algo 
                
                # get temp start point (if BestPred changing then this will be the option)
                tempStartCity = nodes[i]
                
                # get all neighbours of tempStartCity
                NEIGHBORS, DISTANCES = cd.city_neighbors(tempStartCity)
                
                # find cumulative cost of all neighbours
                tempCumCost = []
                currBestPrevCost = bestCumCost[cd.city_index(tempStartCity, city_list=nodes)[0]]
                for n in range(len(NEIGHBORS)):
                    tempCumCost.append(DISTANCES[n] + currBestPrevCost)
                
                # merge cumulative costs and main lists
                for k in range(len(NEIGHBORS)):
                    
                    # get current costs
                    currCity = NEIGHBORS[k]
                    currCumCost = tempCumCost[k]
                    
                    # get costs from main list
                    currIndex = cd.city_index(currCity, city_list=nodes)[0]
                    
                    # currCity may not be in nodes
                    if currIndex == -1:
                        # create a new entry
                        nodes.append(currCity)
                        check.append(False)
                        bestCumCost.append(currCumCost)
                        bestPred.append(tempStartCity)
                    else:
                        # if previously exists then compare and update 
                        prevBestCost = bestCumCost[currIndex]
                        if currCumCost < prevBestCost:
                            check[currIndex] = False
                            bestCumCost[currIndex] = currCumCost
                            bestPred[currIndex] = tempStartCity
                            startFromBegin = True
                
                # the node you are doing all this for, set its check to true
                check[i] = True
                
            if startFromBegin:
                break
        
        # check if we need to break out of big loop
        # get index of destination city
        destiIndex = cd.city_index(DestCity,city_list=nodes)[0]
        
        if (destiIndex != -1):
            destiCheck = check[cd.city_index(DestCity,city_list=nodes)[0]]
            if destiCheck:
                continueBigLoop = False
        
    # get the smallest distance
    DIST = bestCumCost[-1]
    
    # backtrack to get path 
    pathReverse = []
    currentNode = DestCity
    pathReverse.append(currentNode)
    while pathReverse[-1] != OrigCity:
        currentIndex = cd.city_index(currentNode,city_list=nodes)[0]
        pathReverse.append(bestPred[currentIndex])
        currentNode = nodes[cd.city_index(bestPred[currentIndex], city_list=nodes)[0]]
    
    # reverse PATH list
    for element in reversed(pathReverse):
        PATH.append(element)
 
    return PATH, DIST


# define the origin and destination cities
# OrigCity = 'A'; DestCity = 'F'
# OrigCity = 'Seattle'; DestCity = 'Miami'
# OrigCity = 'New Orleans'; DestCity = 'Buffalo'
OrigCity = 'Omaha'; DestCity = 'Brunswick'

# find the best path and the resulting cumulative mileage
PATH, DIST = best_city_path(OrigCity,DestCity)

# print information about the resulting distance
print('The cumulative distance from ' + OrigCity + ' to '
	+ DestCity + ' is ' + str(DIST) + ' miles.')

# display the sequence of cities
print('Shortest travel sequence:')
for k in range(len(PATH)):
	print('- ' + PATH[k])

# plot the city map
fig = plt.figure(figsize=[9,6])
ax = plt.subplot(111)
cd.city_data_plot(cities=True,distances=False)
# draw the best path into the map
cd.city_path_plot(PATH)
# display the result
plt.show()
