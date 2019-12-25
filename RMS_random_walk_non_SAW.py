from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
#Three dimensional random walk, not SAW.

#Calculates and stores all values of the coordinates
def rand_walk(x,y,z,num_of_steps):
    coord = [[0,0,0]]
    
    for i in range(0,num_of_steps-1):
        #A random number between the interval 0-5 is generated
        rand_num = int(np.random.rand()*5)
        
        #Appending walk
        if rand_num == 0: # x += 1
            x[i+1] = x[i]+1
            y[i+1] = y[i]
            z[i+1] = z[i]
            #stores all the coordinates
            coord.append([x[i+1],y[i+1],z[i+1]])
    
        if rand_num == 1: # x -= 1
            x[i+1] = x[i]-1
            y[i+1] = y[i]
            z[i+1] = z[i]
            coord.append([x[i+1],y[i+1],z[i+1]])
        
        if rand_num == 2: # y += 1
            x[i+1] = x[i]
            y[i+1] = y[i]+1
            z[i+1] = z[i]
            coord.append([x[i+1],y[i+1],z[i+1]])
            
        if rand_num == 3: # y -= 1
            x[i+1] = x[i]
            y[i+1] = y[i]-1
            z[i+1] = z[i]
            coord.append([x[i+1],y[i+1],z[i+1]])
    
        if rand_num == 4: # z += 1
            x[i+1] = x[i]
            y[i+1] = y[i]
            z[i+1] = z[i]+1
            coord.append([x[i+1],y[i+1],z[i+1]])
        
        if rand_num == 5: # z -= 1
            x[i+1] = x[i]
            y[i+1] = y[i]
            z[i+1] = z[i]-1
            coord.append([x[i+1],y[i+1],z[i+1]])
    #Return a list of x,y,z,coord
    return x,y,z, coord

#Implementation of Root mean square of end to end distance

#Generate many random walks for a few values of the step number in the range from
#1 to 1000 and determine the root mean squared end-to-end distance sqrt(⟨R2⟩) for each length
    
#A function that calculates the root mean square
#The argument passed into the function is an array with end-to-end distances 
#for multiple iterations of the same step number
def rms_func(arr):
    
    #Store the magnitude of each coordinate
    mag_vals = []    
    #Each coord is appended and the magnitude is calculated
    for i in range(0, len(arr)):
        mag_vals.append(np.linalg.norm(arr[i]))
    #Square every element in the list,sum them, take the mean value and root
    rms = np.sqrt((np.sum(np.square(mag_vals)) / (len(mag_vals))))
    return rms
    

if __name__ == "__main__":
    #Number of steps
    num_of_steps = 100
    
    #Store x,y,z values, note the random walk begins in origo
    x = [0] * num_of_steps
    y = [0] * num_of_steps
    z = [0] * num_of_steps 
    res = rand_walk(x,y,z,num_of_steps)
    
    
    #Number of how many times the random walk shall be calculated
    num_rand = 4
    #Contains the last coordinate of each random walk
    last_coord = []
    for i in range(0,num_rand):
        #Store the total list of x,y,z, coord
        store_val = rand_walk(x,y,z,num_of_steps)
        #Appends last coordinate of each random walk
        last_coord.append(store_val[3][num_of_steps-1])
        
    #Calculating the rms
    print(rms_func(last_coord))
        
    
    
    
    
    
    