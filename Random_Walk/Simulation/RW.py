from IPython import get_ipython
get_ipython().magic('reset -sf')

#Importing measurements from Modules
from Modules import ROG
from Modules import rms
from Modules import rm
from Modules import SEE_R_F
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
#Three dimensional random walk, not SAW.

#Calculates and stores all values of the coordinates
def rand_walk(num_of_steps):
    x = [0] * num_of_steps
    y = [0] * num_of_steps
    z = [0] * num_of_steps
    coord = [[0,0,0]]
    
    for i in range(0,num_of_steps-1):
        #A random number between the interval 0-5 is generated
        rand_num = int(np.random.rand()*6)
        
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

    
    step_num = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    M = 1000
    #For each walk we wanna calculate the rms and rm
    rms_store = []
    rm_store = []
    radius_mean_store = []
    
    


    #För varje antalet steg i step_num skall den itera 10,15,20...
    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        #How many failed attempts
        radius_temp_store= []
        

        #För antalet num_walks/reruns
        for w in range(0,M):
            #Store the total list of x,y,z, coord
            store_val = rand_walk(num_of_step)
            
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
            #Store r_g in radius_store for each rerun
            radius_temp_store.append(ROG(store_val[3]))




        #calls rms with input last_coord
        rms_store.append(rms(last_coord)[0])
        #calls rm with input last_coord
        rm_store.append(rm(last_coord))

        #Nu skall radius_temp_store summeras och delas på antalet reruns
        mean_radius = np.sum(radius_temp_store)/M
        radius_mean_store.append(mean_radius)
    #SEE
    SEE = SEE_R_F(rms_store, rm_store, M)[1]
    ERMSF = SEE_R_F(rms_store, rm_store, M)[0]
    #Note that rms and ROG returns R_F^2 and R_g^2 therefore
    rms_store = np.sqrt(rms_store)
    radius_mean_store = np.sqrt(radius_mean_store)
    #Polymer approximation gives
    approx_val = np.power(step_num,0.50)
    print(SEE)
    print(ERMSF)
    plt.figure()
    plt.plot(step_num,rms_store, c = 'r')
    plt.plot(step_num, radius_mean_store, c = 'b')
    plt.plot(step_num,approx_val, c = 'pink')
    plt.legend(('R_F','R_g','N^(0.5)'))
    plt.title(('R_g and R_F for simple random walk with M = ' + str(M) + ' reruns'))
    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    
    plt.figure()
    plt.plot(step_num,SEE,
             step_num,ERMSF)
    plt.legend(('SEE','ERMSF'))
    plt.title(('SEE and ERMSF for simple random walk with M = ' + str(M) + ' reruns'))
    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    
    
   
    
    
    
    
    
    
    
    
    
    
