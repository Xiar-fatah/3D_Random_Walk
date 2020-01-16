from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#Importing measurements from Modules
from Modules import rms_func
from Modules import rm_func
from Modules import rms_fluc_func
from Modules import err_est_func
from Modules import radius

#Three dimensional random walk, not SAW.

#Calculates and stores all values of the coordinates
def rand_walk(num_of_steps):
    x = [0] * num_of_steps
    y = [0] * num_of_steps
    z = [0] * num_of_steps
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



    
    
if __name__ == "__main__":

    step_num = [100,200,300,400,500,600,700,800,900,1000]
    num_walks = 100
    
    #RMS plot
    #For each walk we wanna calculate the rms and rm
    rms_store = []
    rm_store = []
    radius_mean_store = []
    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        x = [0] * num_of_step
        y = [0] * num_of_step
        z = [0] * num_of_step 
        radius_store = []
        for w in range(0,num_walks):
            #Store the total list of x,y,z, coord
            store_val = rand_walk(x,y,z,num_of_step)
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
            #Calculating each radius of gyration and storing them in radius_store
            radius_store.append(radius(store_val[3]))
        #calls rms_func with input last_coord
        rms_store.append(rms_func(last_coord))
        rm_store.append(rm_func(last_coord))
        
        #Calculating the mean value for each step number and storing them in radius_mean_store
        radius_mean_store.append(np.sum(radius_store)/(len(radius_store)))
        
    #Plot of RMS, RM, RMS fluctuation, SEE, RoG
    plt.figure()
    plt.plot(step_num, rms_store, '-')
#    plt.plot(step_num, rm_store, '-')
#    plt.plot(step_num, rms_fluc_func(rms_store,rm_store,num_walks), '-')
#    plt.plot(step_num, err_est_func(rms_store,rm_store,num_walks), '-')
#    plt.plot(step_num, radius_mean_store, '-')
    plt.legend(("RMS"))


    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
#    ##test
#    x_1 = [0] * 10
#    y_1 = [0] * 10
#    z_1 = [0] * 10
#    res = rand_walk(x_1,y_1,z_1,10)
#    center_val = center(res[3])
#    radius = radius(res[3])
#    
#    print(radius)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
