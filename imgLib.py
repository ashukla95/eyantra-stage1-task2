# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  Cross_A_Crater (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task2
*  Filename: imgLib.py
*  Version: 1.5.0  
*  Date: November 21, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""
#Complete the both function mentioned below, and return the desired outputs
#Additionally you may add your own methods here to help both methods mentioned below
###################Do not add any external libraries#######################
import cv2
import numpy as np
import global_variables as gv
grid_map = []
ls1 = []
def neighbour(x,y):
    ls = []
    if y+1 < 14:
        if grid_map[x][y+1] == 1:
            ls.append((x,y+1))
    if x+1 < 14 and y+1 < 14:
        if grid_map[x+1][y+1] == 1:
            ls.append((x+1,y+1))
    if x+1 < 14:
        if grid_map[x+1][y] == 1:
            ls.append((x+1,y))
            
    if x+1 < 14 and y-1 >-1:
        if grid_map[x+1][y-1] == 1:
            ls.append((x+1,y-1))
    if y-1 > -1:
        if grid_map[x][y-1] == 1:
            ls.append((x,y-1))
            
    if x-1 > -1 and y-1 > -1:
        if grid_map[x-1][y-1] == 1:
            ls.append((x-1,y-1))
            
    if x-1 > -1:
        if grid_map[x-1][y] == 1:
            ls.append((x-1,y))
        
    if x-1 > -1 and y+1 < 14:
        if grid_map[x-1][y+1] == 1:
            ls.append((x-1,y+1))

    return ls 


"""
dist1 = []
dist = []
prev1 = []
prev = []
q = []
graph = []
dist1 = [ 999  for j in range(196) ]
prev1 = [ -1  for j in range(196) ]
row = 0
col = 0
for j in range(14):
    for k in range(14):
        if grid_map[j][k] == 1:
            q.append((j,k))
"""
print "path_global.py"
def op(grid_map,a):         # Dijkstra's algorithm
    #print grid_map
    gv.graph= []
    gv.dist1 = [ [999 for i in range(14)] for j in range(14) ] 
    gv.prev1 = [ [-1 for i in range(14)] for j in range(14) ]
    #dist1 = [ 999  for j in range(196) ]
    #prev1 = [ -1  for j in range(196) ]
    
    for j in range(14):
        for k in range(14):
            if grid_map[j][k] == 1:
                gv.graph1.append((j,k))
    
    #a = 0
    dist = gv.dist1
    gv.prev = gv.prev1
    graph = gv.graph1
    
    dist[13][a] = 0 #source node distance
    row = 999
    col = 999
    destination_reached = 0
    while(len(graph)>0 and (not destination_reached)):
        mium = min_index = 9999
        #....find node in graph with minimum distance.....
        for g in range(len(graph)):                    
            x1 = graph[g][0]
            y1 = graph[g][1]
            
            if dist[x1][y1] < mium:
                mium = dist[x1][y1]
                x = x1
                y = y1
                min_index=g
        #print min_index
        graph.pop(min_index)
        neighbour_list = neighbour(x,y)
        for nl in neighbour_list:
            nlx = nl[0]
            nly = nl[1]
            if nlx == 0:
                destination_reached = 1
                row = nlx
                col = nly
            length_from_node_to_neighbour = 1
            alt = dist[x][y] + length_from_node_to_neighbour
            if alt < dist[nlx][nly]:
                dist[nlx][nly] = alt
                gv.prev[nlx][nly] = (x,y)
    """
    print "prev"
    print gv.prev1
    print "graph"
    print gv.graph1
    """
    return gv.prev ,row ,col


#prev,row,col = op(grid_map,1)
#print row,col
#print prev
#print gv.prev1
route = []
shortest_path = []


def path(x,y,route):
    
    if gv.prev[x][y]==-1:
        return route
    element = gv.prev[x][y]
    x = element[0]
    y = element[1]
    route.append((x,y))           #storing path in route
    path(x,y,route)
    return route



# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)
# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
def detectCellVal(img_gray,grid_map):
        #your code here


        
        #finding the contour points of every provided digit
        
        cellcontour=[0,0]
        for z in range(2):
                imgpath = 'digits/'+str(z)+'.jpg'
                
                im=cv2.imread(imgpath,0)
                img=im[10:40,10:40]
                ret, thresh = cv2.threshold(img, 127, 255,0)
                contours,hierarchy = cv2.findContours(thresh,2,1)
                cellcontour[z] = contours[0]

        
        #im2 = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        # dividing test images in grids and finding the contour points of each grid
        
        for i in range(14):
                for j in range(14):
        
                        x = 50*i
                        y = 50*j
                        img2 = img_gray[x+10:x+40,y+10:y+40]

                        ret, thresh2 = cv2.threshold(img2, 127, 255,0)
                        contours,hierarchy = cv2.findContours(thresh2,2,1)
                        cnt2 = contours[0]
                        # contour matching + storing the object/no in grid map
                        match = -1
                        for z in range(2):
                                ret = cv2.matchShapes(cnt2,cellcontour[z],1,0.0)
                                if (ret == 0.0):
                                        match = z
                                        grid_map[i][j] = match
                             
                                        
                        
                        j += 1
                i += 1

        #print grid_map
        #your code here
        return grid_map
"""
grid_map = [ [ 0 for i in range(14) ] for j in range(14) ]
img_gray = cv2.imread('task2sets/task2_img_1.jpg',0)
grid_map = detectCellVal(img_gray,grid_map)
"""
############################################################################################
# solveGrid finds the shortest path,
# between valid grid cell in the start row 
# and valid grid cell in the destination row 
# solveGrid(grid_map)
# Return the route_path and route_length


def solveGrid(grid_map):
        route_length=0
        route_path=[]
        
        for a in range(14):
                #grid_map = gv.grid_map
                route = []
                if grid_map[13][a] == 1:
                        prev,row,col = op(gv.grid_map,a)
                        route = []
                        route.append((row,col))
                        route = path(row,col,route)
                        print "path......."
                        print route
                        if len(route)<gv.length and len(route)>=13:
                                length = len(route)
                                shortest_path = route
        
        if len(shortest_path)<13:
                shortest_path = []
                shortest_length = 0
        else :
                shortest_length = len(shortest_path)-1
        
        route_length=shortest_length
        route_path=shortest_path
        for i in range(route_length):
                a = route_path[i][0]+1
                b = route_path[i][1]+1
                route_path[i] = (b,a)
        print route_length-1
        return route_path, route_length
                                
                        
grid_map = gv.grid_map        
solveGrid(grid_map)





############################################################################################
