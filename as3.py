from typing import Sized
import csv

import math
import numpy as np
size=100
class CrocMonitor:
    locationList =[]
    import csv
    def __init__(self, size):

        self.locationList = []
        self.matrix = [[0 for x in range(size)]for y in range(size)] # declare for the matrix
        self.points=[]
        self.readData()
        self.storeDistance()
        #
        self.Track=[]
        self.Trace=[] #Trace[v]
        self.paths = []
        self.Start =""
        self.End =""

    # read the data from csv file
    def readData(self):
        with open('Locations.csv') as f:
            csv_reader = csv.reader(f)
            index = 0
            next(csv_reader)
            for line in csv_reader:

                pointName=line[0]
                x=line[1]
                y=line[2]
                number=line[3]
                edge=line[4]

                water=False
                if line[5] == "W":
                    water=True

                self.locationList .append( [pointName,  x, y, number, edge, water] ) # etc

                if not pointName in self.points:

                    self.points.append(pointName)
                index += 1

        f.close()

    # Store distance will store the Start point and end point (Cro sightings adn neightbour point)
    # Tinh va luu khoang cach cua 2 diem gan nhat and add to the matrix
    def storeDistance(self):

        for index in range(0, len(self.locationList)-1): # run all of the data file

            if self.locationList[index][4]!="":
                startpoint = self.locationList[index][0] # take the "Croc sightings" spoint
                endpoint = self.locationList[index][4] # take the "neightbour" point

                for indexa in range (0, len(self.points)-1): # run all of the data in excel
                    if self.points[indexa] == startpoint: # find the start point on the map (Croc sightings)
                        indexPointa=indexa # store the start point on the map (Croc sightings)

                        for indexb in range(0, len(self.points)-1): # run all of the data in excel
                            if self.points[indexb] == endpoint: # find the end point on the map (Croc sightings)
                                indexPointb = indexb # store the start point on the map (Croc sightings)

                                distance = self.computeDistance(startpoint, endpoint) #compute the distance ---- Teacher -----
                                #distance = self.computeDistance(indexPointa, indexPointb) #compute the distance
                           #store distance along path
                                self.matrix[indexa][indexb]= distance
                                self.matrix[indexb][indexa]= distance
                                break
                        break




    # general question (two point not closed in the map) for example from 15 -> 18 by add the a list path such as [15,16,18]
    def computePathDistance (self,path):

        #provide the distance between two points a and b, as the end points on a path. Assume not adjacent
        distance=0
        # ----- Quang Code-----
        for i in range(0,len(path)-1):
            distance= distance + self.computeDistance(path[i], path[i+1]) # calculate the distance of small path

         #----- End Quang Code-----

        return distance

    # Question 2
    # -- will call the function findScope() to find all of the path
    # -- will calculate the distance of all of the find path (computePathDistance)
    # and return the shorest path
    def findPath(self,a,b):
        path=[]
        #returns shortest path a to b
        return path

    # this function will write to find the distance of two closest point (Cro sightings point and neightbour point)
    def computeDistance (self, a, b):

        # provide the distance between two points a and b on a path. Assume adjacent
        distance=0
    #      ----- Quang Code-----

        # a and b is the index (row in the csv) -> xa, ya, xb, yb
        for index in range (0, len(self.locationList)):
            if(self.locationList[index][0] == a):
                indexa = index
                xa = int(self.locationList[indexa][1])
                ya = int(self.locationList[indexa][2])
            if(self.locationList[index][0] == b):
                indexb = index
                xb = int(self.locationList[indexb][1])
                yb = int(self.locationList[indexb][2])

    #calculate the distance
        distance = math.sqrt(math.pow(xb - xa, 2) + math.pow(yb - ya, 2) * 1.0) # based on the Pytago.
        # ----------------------- End Quang code -----------------------

        return distance

#------------------------------------------------------------
        #----- End Quang Code-----
    # Question 1
    # calculate the time --- assume the speeed.
    def computeCosting(self, a, b):
    # unit costs for scanning all points on all paths between two locations and give exhaustive path for rangers to follow, returned as an list
        path=[]
        costing=0
        return costing,path

    # question 2
    def improveDistance (self, a, b):
    #return point blocked as a value on map (eg A1) and scaled increase in distance between points
        point="A1"
        scaledImprovement=0
        return point, scaledImprovement


    # question 3
    def countCroc(self, beach, x):
    #count the number of crocs likely in a x mile radius of a beach. Return an array [location, number]
        number=0
        return number

    # question 3
    def locateOptimalBlockage(self,a,b):
    # return the point blocked eg A1 and the increase in protection provided using some weighting
        point="A1"
        protection=1
        return point, protection

    # question 3
    def minTime(self,a,b):
    #return list of points trevelled and the time required
        path=[]
        return path

    # Question 1 -- find scope will call FindPath() - write functtion DFS() to find all of path
    def DFS(self,a,b):

        # base statement
        indexa = self.points.index(a)
        self.Track[indexa] = True

        for index in range(len(self.points)):
            #check whether it has neighbour and the neighbour is visted or not visted.
            if self.matrix[indexa][index] !=0 and self.Track[index] == False:
                self.Trace[index] = indexa # store the point go to this point 
                if self.points[index] == b:

                    # store the full of the path
                    i = self.Trace[index]

                    arr = []
                    arr.append(b)

                    while   self.points[i] !=  self.startingPoint: #StartingPoint = "15"

                              arr.append(self.points[i])
                              i = self.Trace[i]
                    arr.append(self.startingPoint)
                    arr.reverse()

                    self.paths.append(arr)

                else:
                    self.DFS(self.points[index], b)
                    self.Track[index] = False
                    self.Trace[index] =-1

    # will call the DFS() function to find all of the path and calcuate the distance for each path
    def findScope(self, a, b):
        # ------------------------------------------ Teacher code ---------------------------------------
        #provide start and end point of search, collect points to consider in search
        # pointList=[a,b]

        #find location of a and b in points list
        # for index in range(0, size-1):
        #     if self.points[index]== a:
        #         indexa=index
        #     if self.points[index] == b:
        #         indexb = index
          # ------------------------------------------  ---------------------------------------
        #Find all paths a to b - Select direct routes only, no cycles or backtracking
        self.DFS(a,b)
        # to print all of the path.
        print("The total path to go from a to b is : ", len(self.paths))

        for i in range(0,len(self.paths)):
            print(self.paths[i])
            # compute the distance for each path
        print("----------------------The distance for each path is: -----------------")
        for i in range(0,len(self.paths)):
            print("The distance of path", self.paths[i], "is", self.computePathDistance(self.paths[i]))
            # print(self.computePathDistance(self.paths[i]))
        # for p in self.paths:
        #     print(p)

        #Find shortest route from path options

        # Add side points to inspect
        #include all nodes that are linked to (neighbour of) any internal point on path (ie point crocodiles can enter)
        #       between a and b - this may add backtracking

        #Example findScope ("15","18")
            #paths are [15,16,18] and [15,16,17,19,20]
            #shortest path [15,16,18]
            #add neighbours [15,16,17,18]

        #This is the exhaustive list of points rangers need to inspect
        # return pointList

if __name__ == '__main__':

    cm=CrocMonitor(size)
    #print (cm.locationList)
    #Changed examples
    cm.computeCosting("15","18")

    print("--------------DFS------------------")
    cm.Track = [False]*(len(cm.points))
    cm.Trace = [-1]*(len(cm.points))
    cm.startingPoint="15"
    print("Find the distance from a to b: 15 -> 18")
    cm.findScope("15", "18") # just try function will user input later.



# --------------------------------------------------------------- Teacher code ------------------------------------------------------
    # exhaustive path is  [15,16, 17,16, 18] so return the length of this as unit cost - note data changes in Locations.csv
    #algorithm to find scope of spanning tree is provided as findScope()
    cm.improveDistance("15","18")
    #output will be 16  Ratio is "original distance on [15,16,18]:0"
    cm.locateOptimalBlockage("15", "A1")
    #returns 16 as other routes have alternative paths
    #may use other data to decide optimum path, but explain in requirements for this method
    cm.minTime("15", "18")
    #returns [15,16,18] and time to travel that path

# --------------------------------------------------------------- End ------------------------------------------------------




    # Call the distance function
    # print("the distance between a and b is: ")
    # print(cm.computeDistance("1","2"))