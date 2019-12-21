# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib qt, for interactive
#Three dimensional random walk, freely jointed chain, SAW

#Number of steps
num_of_steps = 10

#Store x,y,z values, note the random walk begins in origo
x = [0] 
y = [0] 
z = [0]

#A function that generates a random vector and normalizes it
def rand_vec():
    #vec[0] = x, vec[1] = y ....
    vec = []
    for i in range(0,3):
        vec.append(np.random.normal(0,1,1))
    
    norm = np.sqrt(pow(vec[0],2) + pow(vec[1],2) + pow(vec[2],2))
    np.multiply(vec,norm**(-1))
    return vec

#Random walk
for i in range(0,num_of_steps):
    
    vec = rand_vec()
    
    x.append(vec[0])
    y.append(vec[1])
    z.append(vec[2])

#Three dimensional plot mabye try to plot in matlab instead? 
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, 'red')
