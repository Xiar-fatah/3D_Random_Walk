# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib qt, for interactive
#Three dimensional random walk, SAW.

#Number of steps
num_of_steps = 100

#Store x,y,z values, note the random walk begins in origo
x = [0] * num_of_steps
y = [0] * num_of_steps
z = [0] * num_of_steps 

#Store the coordinates, the first coordinate will be in the origo
coord = [[0,0,0]]


#For SAW the random walk needs to check previous steps

Bool = True
i = 0
while Bool:
    #A random number between the interval 0-5 is generated
    rand_num = int(np.random.rand()*5)
    
    if rand_num == 0: # x += 
        #Checks if the next coordinates are in coord, if true rerun with new rand_num
        if [x[i]+1,y[i],z[i]] in coord:
            i -= 1
        #Else if next coordinates are not in coord, store values
        else:
            x[i+1] = x[i]+1
            y[i+1] = y[i]
            z[i+1] = z[i]
            #Stores the coordinates in the format [0, 0, 0]
            coord.append([x[i+1], y[i+1], z[i+1]])
        
    if rand_num == 1: # x -= 1
        if [x[i]-1,y[i],z[i]] in coord:
            i -= 1
        else:
            x[i+1] = x[i]-1
            y[i+1] = y[i]
            z[i+1] = z[i]
            coord.append([x[i+1], y[i+1], z[i+1]])
            
    if rand_num == 2: # y += 1
        if [x[i],y[i]+1,z[i]] in coord:
            i -= 1
        else:
            x[i+1] = x[i]
            y[i+1] = y[i]+1
            z[i+1] = z[i]
            coord.append([x[i+1], y[i+1], z[i+1]])
            
    if rand_num == 3: # y -= 1
        if [x[i],y[i]-1,z[i]] in coord:
            i -= 1
        else:
            x[i+1] = x[i]
            y[i+1] = y[i]-1
            z[i+1] = z[i]
            coord.append([x[i+1], y[i+1], z[i+1]])
            
    if rand_num == 4: # z += 1
        if [x[i],y[i],z[i]+1] in coord:
            i -= 1
        else:
            x[i+1] = x[i]
            y[i+1] = y[i]
            z[i+1] = z[i]+1
            coord.append([x[i+1], y[i+1], z[i+1]])
            
    if rand_num == 5: # z -= 1
        if [x[i],y[i],z[i]-1] in coord:
            i -= 1
        else:
            x[i+1] = x[i]
            y[i+1] = y[i]
            z[i+1] = z[i]-1
            coord.append([x[i+1], y[i+1], z[i+1]])
    i += 1
    
    #If number of values in coord is equal to num_of_steps, stop
    if i == num_of_steps-1:
        Bool = False


#Check if there exist a duplicate in the coord list
for i in range(0, len(coord)):
    for w in range(0,len(coord)):
        if coord[i] == coord[w] and i != w:
            raise Exception('A duplicate was found')
#Three dimensional plot mabye try to plot in matlab instead? 
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'red')
