

#import numpy as np
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
    prev = gv.prev1
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
                prev[nlx][nly] = (x,y)
    """
    print "prev"
    print gv.prev1
    print "graph"
    print gv.graph1
    """
    return prev ,row ,col


#prev,row,col = op(grid_map,1)
#print row,col
#print prev
#print gv.prev1
route = []
shortest_path = []

length = 999
def path(x,y,route):
    
    if prev[x][y]==-1:
        return route
    element = prev[x][y]
    x = element[0]
    y = element[1]
    route.append((x,y))           #storing path in route
    path(x,y,route)
    return route
   
for a in range(14):
    grid_map = gv.grid_map
    route = []
    if grid_map[13][a] == 1:
        prev,row,col = op(gv.grid_map,a) 
        #print row,col
        #print prev
        route = []
        route.append((row,col))
        route = path(row,col,route)
        print "path......."
        print route
        
        if len(route)<length and len(route)>=13:
            length = len(route)
            shortest_path = route
if len(shortest_path)<13:
    shortest_path = []
    shortest_length = 0
else :
    shortest_length = len(shortest_path)-1
print "\nshortest path is:"
print shortest_path
print "length is:"
print shortest_length






            
            
                                    

