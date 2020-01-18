from IPython import get_ipython
get_ipython().magic('reset -sf')
from FJC_SAW import rand_walk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#Importing measurements from Modules
from Modules import ROG
from Modules import rms

if __name__ == "__main__":
    

    step_num = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
#    step_num = [10,20,30]
    M = 10
    r = [0.1,0.09,0.08,0.07]
    #Store the R_g for various radius
    R_g_store = []
    #Store the R_F for various radius
    R_F_store = []
    #Store the average amount of fails for M reruns for each step number
    counter_radius_store = []
    for radius in r:
        #Store counter or the amount of successful walks
        counter_store = []
        
        #For each walk we wanna calculate the rms and rm
        rms_store = []
        radius_mean_store = []
        
    
        #För varje antalet steg i step_num skall den itera 10,15,20...
        for num_of_step in step_num:
            #Temporary store the count to take the average value
            count = []
            #Contains the last coordinate of each random walk and resets each for walk
            last_coord = []
            #How many failed attempts
            radius_temp_store= []
    
            #För antalet num_walks/reruns
            for w in range(0,M):
                #Store the total list of x,y,z, coord
                store_val = rand_walk(num_of_step, radius)
                #Appends the amount of failed runs
                count.append(store_val[4])
                #Appends last coordinate of each random walk
                last_coord.append(store_val[3][num_of_step-1])
                #Store r_g in radius_store for each rerun
                radius_temp_store.append(ROG(store_val[3]))
        
            #Takes the average of the count
            counter_store.append(np.sum(count)/len(count))
            #calls rms_func with input last_coord
            rms_store.append(rms(last_coord)[0])
     
            #Nu skall radius_temp_store summeras och delas på antalet reruns
            mean_radius = np.sum(radius_temp_store)/M
            radius_mean_store.append(mean_radius)
        
        counter_radius_store.append(counter_store)
        R_F_store.append(rms_store)
        R_g_store.append(radius_mean_store)
    #We wanna find the flory exponent
    #Flory exponent 6*R_g^2/R_F = 1
    flory = []
    for i in range(0,len(r)):
        flory_r_temp_val= []
        for w in range(0,len(step_num)):
            flory_r_temp_val.append(6*R_g_store[i][w]/R_F_store[i][w])
        flory.append(flory_r_temp_val)
            
        
    R_F_store = np.sqrt(R_F_store)
    R_g_store = np.sqrt(R_g_store)
    
    #Plot for R_F
    plt.figure()
    plt.plot(step_num, R_F_store[0][0:len(step_num)],
             step_num, R_F_store[1][0:len(step_num)],
             step_num, R_F_store[2][0:len(step_num)])
    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    plt.legend(('r = ' + str(r[0]),'r =' + str(r[1]),'r =' + str(r[2]), 'r = ' +str(r[3])))
    plt.title(('R_F for various r and for M = ' + str(M)))
    #Plot for R_g
    plt.figure()
    plt.plot(step_num, R_g_store[0][0:len(step_num)],
             step_num, R_g_store[1][0:len(step_num)],
             step_num, R_g_store[2][0:len(step_num)])
    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    plt.legend(('r = ' + str(r[0]),'r =' + str(r[1]),'r =' + str(r[2]), 'r = ' +str(r[3])))
    plt.title(('R_g for various r and for M = ' + str(M)))
    #Plot for flory
    plt.figure()
    plt.plot(step_num, flory[0][0:len(step_num)], '.',
             step_num, flory[1][0:len(step_num)],'.',
             step_num, flory[2][0:len(step_num)], '.')
    plt.xlabel('Number of steps')
#    plt.ylabel('')
    plt.legend(('r = ' + str(r[0]),'r =' + str(r[1]),'r =' + str(r[2]), 'r = ' +str(r[3])))
    plt.title(('Flory exponent for M = ' + str(M)))
#    Plot for fraction of success
#    plt.figure()
#    plt.plot(step_num, np.reciprocal(counter_radius_store[0][0:len[step_num]]),
#             step_num, np.reciprocal(counter_radius_store[1][0:len[step_num]]),
#             step_num, np.reciprocal(counter_radius_store[2][0:len[step_num]]))
#    plt.xlabel('Number of steps')
#    plt.ylabel('Fraction of Success')
#    plt.title('Fraction of success for ' + str(M) + ' reruns.')
#    plt.figure()
#    plt.plot(step_num, counter_store, c = 'r')
#    plt.xlabel('Number of steps')
#    plt.ylabel('Amount of tries')
#    plt.title('Amount of tries for ' + str(M) + ' reruns.')
#   

    