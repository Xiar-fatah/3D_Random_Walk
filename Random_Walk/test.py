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

def rand_walk(N):
    
    coord = [[0,0,0]]
    Done = False
    #Skapar en vektor med np.random.normal(0,1,1)
    Dir=[0,0,0]
    
    while Done == False:
        #x,y,z koordinaterna
        xList=[0]
        yList=[0]
        zList=[0]
        #
        PosList=[[0,0,0]]
        
        pos=[0,0,0]
        i=0
        LastDir=[0,0,0]
        while i < N:
            
            Dir[0]=np.random.normal(0,1,1)
            Dir[1]=np.random.normal(0,1,1)
            Dir[2]=np.random.normal(0,1,1)
            Dir=np.divide(Dir,(Dir[1]**2+Dir[2]**2+Dir[0]**2)**0.5)
        
            pos[0] = pos[0] + Dir[0]
            pos[1] = pos[1] + Dir[1]
            pos[2] = pos[2] + Dir[2]
           
            PosList.append([pos[0], pos[1], pos[2]])
            xList.append(pos[0])
            yList.append(pos[1])
            zList.append(pos[2])
            coord.append([pos[0],pos[1],pos[2]])
            if i == N-1:
                Done = True
            i = i + 1
    return xList,yList,zList,coord
        
if __name__ == "__main__":
    step_num = [10,50,100,200,300,400,500,600,700,800]
    test = np.sqrt(step_num)
    num_walks = 20
    
    res = rand_walk(3)
#    print(res[0])
#    print(res[1])
#    print(res[2])
#    print(res[3])

    #For each walk we wanna calculate the rms and rm
    rms_store = []
    rm_store = []
    radius_mean_store = []

    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        radius_store = []

        for w in range(0,num_walks):
            #Store the total list of x,y,z, coord
            store_val = rand_walk(num_of_step)
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
            radius_store.append(radius(store_val[3]))


        #calls rms_func with input last_coord
        rms_store.append(rms_func(last_coord))
        rm_store.append(rm_func(last_coord))
        radius_mean_store.append(np.sum(radius_store)/(len(radius_store)))

#        
    #Plot of RMS, RM, RMS, SEE fluctuation
    plt.figure()
    plt.plot(step_num, rms_store, '-')
    plt.plot(step_num,test)
#    plt.plot(step_num, rm_store, '-')
#    plt.plot(step_num, rms_fluc_func(rms_store,rm_store,num_walks), '-')
#    plt.plot(step_num, err_est_func(rms_store,rm_store,num_walks), '-')
#    plt.plot(step_num, radius_mean_store, '-')
#    plt.legend(("RMS", "RM", "RMS fluctuation", "SEE","RoG"))
#    plt.xlabel('Number of steps')
#    plt.ylabel('Distance')
#    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
#    
#    plt.xlabel('Number of steps')
#    plt.ylabel('Distance')
#    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
#    
