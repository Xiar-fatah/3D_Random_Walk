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
import random
#%matplotlib qt, for interactive


#Three dimensional random walk, SAW.
def SAW(n):
    count=0

    DirList = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]];
    Boolean = False
    while Boolean == False:
        x = [0]
        y = [0]
        z = [0]
        coord = [[0, 0, 0]]
        pos = [0, 0, 0]
        i = 0
        LastDir = [0, 0, 0]
        while i < n:
            if LastDir == [0, 0, 0]:
                Dir = random.choice(DirList)
            else:
                TempDirList = DirList.copy()
                TempDirList.remove(LastDir)
                Dir = random.choice(TempDirList)
            for j in range(0, 3):
                LastDir[j] = -Dir[j]
            pos[0] = pos[0] + Dir[0]
            pos[1] = pos[1] + Dir[1]
            pos[2] = pos[2] + Dir[2]
            if pos in coord:
                count=count+1
                break
            coord.append([pos[0], pos[1], pos[2]])
            x.append(pos[0])
            y.append(pos[1])
            z.append(pos[2])
            if i == n-1:
                Boolean = True
            i = i + 1
    return x,y,z, coord, count
            
if __name__ == "__main__":

    
    step_num = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100]
    M = 1000
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
            store_val = SAW(num_of_step)
            
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
    
    #SEE
    SEE = SEE_R_F(rms_store, rm_store, M)[1]
    ERMSF = SEE_R_F(rms_store, rm_store, M)[0]
    print(SEE)
    print(ERMSF)
    #Note that rms and ROG returns R_F^2 and R_g^2 therefore
    rms_store = np.sqrt(rms_store)
    radius_mean_store = np.sqrt(radius_mean_store)
    #Polymer approximation gives
    approx_val = np.power(step_num,0.592)
    plt.figure()
    plt.plot(step_num,rms_store, c = 'r')
    plt.plot(step_num, radius_mean_store, c = 'b')
    plt.plot(step_num,approx_val, c = 'pink')
    plt.legend(('R_F','R_g','N^(0.592)'))
    plt.title(('R_g and R_F for self avoiding random walk with M = ' + str(M) + ' reruns'))
    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    



    