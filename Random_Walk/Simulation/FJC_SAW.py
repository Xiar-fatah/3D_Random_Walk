from IPython import get_ipython
get_ipython().magic('reset -sf')

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#Importing measurements from Modules
from Modules import ROG
from Modules import rms
from Modules import rm
from Modules import SEE_R_F
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
    step_num = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
#    step_num = [10,20]
    M = 1000
    r = 0.07 #Radius of the sphere

    

    #For each walk we wanna calculate the rms and rm
    rms_store = []
    radius_mean_store = []    
    rm_store = []

    
    
    #Store counter or the amount of successful walks
    counter_store = []

    #För varje antalet steg i step_num skall den itera 10,15,20...
    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        #How many failed attempts
        radius_temp_store= []
        #Temporary store the count to take the average value
        count = []

        #För antalet num_walks/reruns
        for w in range(0,M):
            #Store the total list of x,y,z, coord
            store_val = rand_walk(num_of_step, r)
            
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
            #Store r_g in radius_store for each rerun
            radius_temp_store.append(ROG(store_val[3]))
            #Appends the amount of failed runs
            count.append(store_val[4])

        #Takes the average of the count
        counter_store.append(np.sum(count)/len(count))

        #calls rms_func with input last_coord
        rms_store.append(rms(last_coord)[0])
        rm_store.append(rm(last_coord))

        #Nu skall radius_temp_store summeras och delas på antalet reruns
        mean_radius = np.sum(radius_temp_store)/M
        radius_mean_store.append(mean_radius)
        
    SEE = SEE_R_F(rms_store, rm_store, M)[1]
    ERMSF = SEE_R_F(rms_store, rm_store, M)[0]
    print(SEE)
    print(ERMSF)
    #Dubbelkollar så att 6*R_g^2/R_F^2 = 1
    for i in range(0,len(radius_mean_store)):
        print((6*radius_mean_store[i])/(rms_store[i]))


    plt.plot(step_num, np.reciprocal(counter_store), color = 'red')




















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    #Plot for fraction of success
#    plt.figure()
#    plt.plot(step_num, np.reciprocal(counter_store), '-')
#    plt.xlabel('Number of steps')
#    plt.ylabel('Fraction of Success')
#    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
    
