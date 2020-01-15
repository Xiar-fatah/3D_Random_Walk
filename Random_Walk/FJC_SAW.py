from IPython import get_ipython
get_ipython().magic('reset -sf')

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#Importing measurements from Modules
from Modules import rms_func
from Modules import rm_func
from Modules import rms_fluc_func
from Modules import err_est_func
from Modules import radius

def rand_vec(): #Generates a normalized 3d vector with the help of np.random.normal(0,1,1)
    #vec[0] = x, vec[1] = y ....
    vec = []
    for i in range(0,3):
        vec.append(np.random.normal(0,1,1))
    vec = np.divide(vec,(vec[1]**2+vec[2]**2+vec[0]**2)**0.5)
    return vec
def summation(vec_len, vec): #Adds the newly generated vec to vec_len
    for i in range(0,3):
        vec_len[i] = vec_len[i] + vec[i]
    return vec_len

def rand_walk(num_of_step, r):
    
            
    Boolean = False
    fails = 0

    while Boolean == False:
        x = [0]
        y = [0]
        z = [0]
        coord = [[0,0,0]] #Stores [x,y,z]
        vec_len = [0,0,0] #Sum of x,y,z vecs, needed to compare the spheres 
        i = 0
        while i < num_of_step:
            counter = 0    
            vec = rand_vec() #Rand_vec generates a normalized vector
            vec_len = summation(vec_len, vec) #Adds each coordinate of vec to vec_len

            for coordinates in coord: #Each x,y,z coordinate in coord is compared to the newly obtained vec_len coordinates
                if (vec_len[0]-coordinates[0])**2+(vec_len[1]-coordinates[1])**2+(vec_len[2]-coordinates[2])**2 < (2*r)**2:   
                    counter += 1

            if counter > 0:
                fails += 1
                break #Breaks out of while i < num_of_step: and restarts
            coord.append([vec_len[0], vec_len[1], vec_len[2]])
            x.append(vec_len[0])
            y.append(vec_len[1])
            z.append(vec_len[2])
            if i == num_of_step-1:
                Boolean = True
            i = i + 1      
    return x, y, z, coord, fails
    
if __name__ == "__main__":
    step_num = [10,30,50,70,100,200]
#    step_num = [10,20]
    num_walks = 20
    r = 0.1 #Radius of the sphere


    #For each walk we wanna calculate the rms and rm
    rms_store = []
    rm_store = []
    radius_mean_store = []
    counter_store = []
    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        radius_store = []
        count = []
        for w in range(0,num_walks):
            #Store the total list of x,y,z, coord
            store_val = rand_walk(num_of_step, r)
            
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
            radius_store.append(radius(store_val[3]))
            count.append(store_val[4])
        #calls rms_func with input last_coord
        counter_store.append(np.sum(count)/len(count))
        rms_store.append(rms_func(last_coord))
        rm_store.append(rm_func(last_coord))
        radius_mean_store.append(np.sum(radius_store)/(len(radius_store)))
    #Plot of RMS, RM, RMS, SEE fluctuation
    plt.figure()
    plt.plot(step_num, rms_store, '-')
    
    #Plot for fraction of success
    plt.figure()
    plt.plot(step_num, np.reciprocal(counter_store), '-')
    plt.xlabel('Number of steps')
    plt.ylabel('Fraction of Success')
    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
    
