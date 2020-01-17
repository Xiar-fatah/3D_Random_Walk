from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#Importing measurements from Modules
from Modules import rms
from Modules import rm
from Modules import ROG
from Modules import SEE_R_F
#Freely jointed chain, Non SAW

def rand_walk(n):
    coord = [[0,0,0]]
    x = [0]
    y = [0]
    z = [0]
    for i in range(0,n):
        
        #Generates a normalized random vector
        vec = rand_vec()
        
        #Appends the normalized random vector
        x.append(vec[0] + x[i])
        y.append(vec[1] + y[i])
        z.append(vec[2] + z[i])
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
    step_num = [10,20,30,40,50,60,70,80,90,100]
    #step_num = [10,20]
    test = np.sqrt(step_num)
    num_walks = 1000
    

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
            radius_store.append(ROG(store_val[3]))

        #calls rms_func with input last_coord
        rms_store.append(rms(last_coord)[0])
        rm_store.append(rm(last_coord))
        radius_mean_store.append(np.sum(radius_store)/(len(radius_store)))
    
    
    SEE = SEE_R_F(rms_store,rm_store,num_walks)
    plt.plot(step_num,SEE)

    #Plot of RMS, RM, RMS, SEE fluctuation
    plt.figure()
    plt.plot(step_num, rms_store, '-')
    plt.title("FJC-NON-SAW for " + str(num_walks) + " reruns" )
    plt.xlabel('x')
    plt.ylabel('y')
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
    plt.plot(step_num,test)
    
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
