from IPython import get_ipython
get_ipython().magic('reset -sf')
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
#Importing measurements from Modules
from Modules import rms_func
from Modules import rm_func
from Modules import rms_fluc_func
from Modules import err_est_func
from Modules import radius


def rand_walk(n):
        
    count=0
    DirList = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]];
    Done = False
    while Done == False:
        xList = [0]
        yList = [0]
        zList = [0]
        PosList = [[0, 0, 0]]
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
            if pos in PosList:
                count=count+1
                break
            PosList.append([pos[0], pos[1], pos[2]])
            xList.append(pos[0])
            yList.append(pos[1])
            zList.append(pos[2])
            if i == n-1:
                Done = True
            i = i + 1
    print(xList)
    return xList,yList,zList,PosList,count

if __name__ == "__main__":
    

    step_num = [10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
    num_walks = 20
    


    #For each walk we wanna calculate the rms and rm
    rms_store = []
    rm_store = []
    counter_store = []
    radius_mean_store = []

    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        #Store counter values temporary
        count = []
        radius_store = []

        for w in range(0,num_walks):
            #Store the total list of x,y,z, coord
            store_val = rand_walk(num_of_step)
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
            count.append(store_val[4])
            #Calculating each radius of gyration and storing them in radius_store

            radius_store.append(radius(store_val[3]))

        counter_store.append(np.sum(count)/len(count))
            
        #calls rms_func with input last_coord
        rms_store.append(rms_func(last_coord))
        rm_store.append(rm_func(last_coord))
        
         #Calculating the mean value for each step number and storing them in radius_mean_store
        radius_mean_store.append(np.sum(radius_store)/(len(radius_store)))
        
        
    #Plot of RMS, RM, RMS, SEE fluctuation
    plt.figure()
    plt.plot(step_num, rms_store, '-')
