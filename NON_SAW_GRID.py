# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#Three dimensional random walk

#Number of steps
num_of_steps = 10

#Store x,y,z values, note the random walk begins in origo
x = [0] * num_of_steps
y = [0] * num_of_steps
z = [0] * num_of_steps 
for i in range(0,num_of_steps-1):
    #A random number between the interval 0-5 is generated
    rand_num = int(np.random.rand()*5)
    
    #Appending walk
    if rand_num == 0: # x += 1
        x[i+1] = x[i]+1
        y[i+1] = y[i]
        z[i+1] = z[i]

    if rand_num == 1: # x -= 1
        x[i+1] = x[i]-1
        y[i+1] = y[i]
        z[i+1] = z[i]
    
    if rand_num == 2: # y += 1
        x[i+1] = x[i]
        y[i+1] = y[i]+1
        z[i+1] = z[i]
        
    if rand_num == 3: # y -= 1
        x[i+1] = x[i]
        y[i+1] = y[i]-1
        z[i+1] = z[i]

    if rand_num == 4: # z += 1
        x[i+1] = x[i]
        y[i+1] = y[i]
        z[i+1] = z[i]+1
    
    if rand_num == 5: # z -= 1
        x[i+1] = x[i]
        y[i+1] = y[i]
        z[i+1] = z[i]-1

print(x,y,z)
#Three dimensional plot mabye try to plot in matlab instead? 
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'red')
