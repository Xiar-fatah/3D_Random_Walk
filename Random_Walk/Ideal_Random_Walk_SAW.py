from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib qt, for interactive
from Modules import rms_func
from Modules import rm_func
from Modules import rms_fluc_func
#Three dimensional random walk, SAW.


#For SAW the random walk needs to check previous steps
def SAW(x,y,z,n):
    #Store the coordinates, the first coordinate will be in the origo
    coord = [[0,0,0]]
    counter = 0
    
    Bool = True
    i = 0
    while Bool:
        #A random number between the interval 0-5 is generated
        rand_num = int(np.random.rand()*5)
        
        if rand_num == 0: # x += 
            #Checks if the next coordinates are in coord, if true rerun with new rand_num
            if [x[i]+1,y[i],z[i]] in coord:
                i = 0
                counter += 1
                coord = [[0,0,0]]
                x = [0] * n
                y = [0] * n
                z = [0] * n
            #Else if next coordinates are not in coord, store values
            if [x[i]+1,y[i],z[i]] not in coord:
                x[i+1] = x[i]+1
                y[i+1] = y[i]
                z[i+1] = z[i]
                #Stores the coordinates in the format [0, 0, 0]
                coord.append([x[i+1], y[i+1], z[i+1]])
            
        if rand_num == 1: # x -= 1
            if [x[i]-1,y[i],z[i]] in coord:
                i = 0
                counter += 1
                coord = [[0,0,0]]
                x = [0] * n
                y = [0] * n
                z = [0] * n
            if [x[i]-1,y[i],z[i]] not in coord:
                x[i+1] = x[i]-1
                y[i+1] = y[i]
                z[i+1] = z[i]
                coord.append([x[i+1], y[i+1], z[i+1]])
                
        if rand_num == 2: # y += 1
            if [x[i],y[i]+1,z[i]] in coord:
                i = 0
                counter += 1
                coord = [[0,0,0]]
                x = [0] * n
                y = [0] * n
                z = [0] * n
            if [x[i],y[i]+1,z[i]] not in coord:
                x[i+1] = x[i]
                y[i+1] = y[i]+1
                z[i+1] = z[i]
                coord.append([x[i+1], y[i+1], z[i+1]])
                
        if rand_num == 3: # y -= 1
            if [x[i],y[i]-1,z[i]] in coord:
                i = 0
                counter += 1
                coord = [[0,0,0]]
                x = [0] * n
                y = [0] * n
                z = [0] * n
            if [x[i],y[i]-1,z[i]] not in coord:
                x[i+1] = x[i]
                y[i+1] = y[i]-1
                z[i+1] = z[i]
                coord.append([x[i+1], y[i+1], z[i+1]])
                
        if rand_num == 4: # z += 1
            if [x[i],y[i],z[i]+1] in coord:
                i = 0
                counter += 1
                coord = [[0,0,0]]
                x = [0] * n
                y = [0] * n
                z = [0] * n
            if [x[i],y[i],z[i]+1] not in coord:
                x[i+1] = x[i]
                y[i+1] = y[i]
                z[i+1] = z[i]+1
                coord.append([x[i+1], y[i+1], z[i+1]])
                
        if rand_num == 5: # z -= 1
            if [x[i],y[i],z[i]-1] in coord:
                i = 0
                counter += 1
                coord = [[0,0,0]]
                x = [0] * n
                y = [0] * n
                z = [0] * n
            if [x[i],y[i],z[i]-1] not in coord:
                x[i+1] = x[i]
                y[i+1] = y[i]
                z[i+1] = z[i]-1
                coord.append([x[i+1], y[i+1], z[i+1]])
        i += 1
        
        #If number of values in coord is equal to num_of_steps, stop
        
        if i == n-1:
            Bool = False
    return x,y,z,coord,counter



if __name__ == "__main__":
    
#    num_of_step = 30
#    x = [0] * num_of_step
#    y = [0] * num_of_step
#    z = [0] * num_of_step 
#    res = SAW(x,y,z,num_of_step)
#    print('x ' + str(res[0]))
#    print('y ' + str(res[1]))
#    print('z ' + str(res[2]))
#    print(res[3])
    step_num = [10,20,30,40,50]
    num_walks = 50
    
    #RMS plot
    #For each walk we wanna calculate the rms

    #RMS plot
    #For each walk we wanna calculate the rms and rm
    rms_store = []
    rm_store = []
    counter_store = []
    for num_of_step in step_num:
        #Contains the last coordinate of each random walk and resets each for walk
        last_coord = []
        #Store counter values temporary
        count = []
        x = [0] * num_of_step
        y = [0] * num_of_step
        z = [0] * num_of_step 
        for w in range(0,num_walks):
            #Store the total list of x,y,z, coord
            store_val = SAW(x,y,z,num_of_step)
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
            count.append(store_val[4])
        counter_store.append(np.sum(count)/len(count))
            
        #calls rms_func with input last_coord
        rms_store.append(rms_func(last_coord))
        rm_store.append(rm_func(last_coord))
        
    #Plot of RMS, RM, RMS fluctuation
    plt.figure()
    plt.plot(step_num, rms_store, '-')
    plt.plot(step_num, rm_store, '-')
    plt.plot(step_num, rms_fluc_func(rms_store,rm_store), '-')
    #plt.plot(step_num, rms_fluc_func(rms_store,rm_store), '-')
    plt.legend(("RMS", "RM", "RMS fluctuation"))

    plt.xlabel('Number of steps')
    plt.ylabel('Distance')
    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
    
    plt.figure()
    plt.plot(step_num, np.reciprocal(counter_store), '-')
    plt.xlabel('Number of steps')
    plt.ylabel('Fraction of Success')
    plt.title('Measurements for ' + str(num_walks) + ' reruns.')
    
        
#    #Check if there exist a duplicate in the coord list
#    for i in range(0, len(res[3])):
#        for w in range(0,len(res[3])):
#            if res[i] == res[w] and i != w:
#                raise Exception('A duplicate was found')
#    Three dimensional plot mabye try to plot in matlab instead? 
#    fig = plt.figure()
#    ax = plt.axes(projection='3d')
#    ax.plot3D(res[0], res[1], res[2], 'red')
#    ax.set_xlabel('x')
#    ax.set_ylabel('y')
#    ax.set_zlabel('z')
