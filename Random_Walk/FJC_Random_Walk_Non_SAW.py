from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

from Modules import rms_func
from Modules import rm_func
from Modules import rms_fluc_func
#Self avoiding walk, freely jointed chain

def rand_walk(x,y,z,n):
    coord = [[0,0,0]]
    for i in range(0,n):
        
        vec = rand_vec()

        x.append(x[i]+vec[0])
        y.append(y[i]+vec[1])
        z.append(z[i]+vec[2])
        coord.append([x[i+1],y[i+1],z[i+1]])

        
    
    return x,y,z,coord

    
#A function that generates a random vector and normalizes it
#Intuitive, a new direction is created
def rand_vec():
    #vec[0] = x, vec[1] = y ....
    vec = []
    for i in range(0,3):
        vec.append(np.random.normal(0,1,1))
    
    norm = np.sqrt(pow(vec[0],2) + pow(vec[1],2) + pow(vec[2],2))
    vec = np.multiply(vec,norm**(-1))
    return vec


    
if __name__ == "__main__":
    step_num = [10,50]
    num_walks = 10
    
    #RMS plot
    #For each walk we wanna calculate the rms

    #RMS plot
    #For each walk we wanna calculate the rms and rm
    rms_store = []
    rm_store = []
    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        x = [0]
        y = [0] 
        z = [0] 
        for w in range(0,num_walks):
            #Store the total list of x,y,z, coord
            store_val = rand_walk(x,y,z,num_of_step)
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
        #calls rms_func with input last_coord
        rms_store.append(rms_func(last_coord))
        rm_store.append(rm_func(last_coord))
    print('rms ' + str(rms_store))
    print('rm ' + str(rm_store))
        
    #Plot of RMS, RM, RMS fluctuation
    plt.plot(step_num, rms_store, '-')
    plt.plot(step_num, rm_store, '-')
    plt.plot(step_num, rms_fluc_func(rms_store,rm_store), '-')
    #plt.plot(step_num, rms_fluc_func(rms_store,rm_store), '-')
    plt.legend(("RMS", "RM", "RMS fluctuation"))

    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
    
    #Three dimensional plot mabye try to plot in matlab instead? 
#    fig = plt.figure()
#    ax = fig.gca(projection='3d')
#    ax.plot(res[0], res[1], res[2], linestyle = '-')
#    ax2 = fig.gca(projection='3d')
#    ax2.scatter([0], [0], [0], c = 'r', marker = 'x')
#    plt.legend(['Polymer', 'Origin'])
#    ax.set_xlabel('x')
#    ax.set_ylabel('y')
#    ax.set_zlabel('z')
#    
#    plt.show()
