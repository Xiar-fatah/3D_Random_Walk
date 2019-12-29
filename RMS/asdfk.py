from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

#Self avoiding walk, freely jointed chain

def rand_walk(x,y,z,n):
    for i in range(0,n):
            
        vec = rand_vec()

        x.append(x[i]+vec[0])
        y.append(y[i]+vec[1])
        z.append(z[i]+vec[2])
    
    return x,y,z

    
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


    
    print(rms_store)
if __name__ == "__main__":
    step_num = [10,50,100,200,300,400,500]
    num_walks = 30
    
    #RMS plot
    #For each walk we wanna calculate the rms


    rms_store = []
    for num_of_step in step_num:
        #Contains the last coordinate of each random walk
        last_coord = []
        x = [0] * num_of_step
        y = [0] * num_of_step
        z = [0] * num_of_step 
        for w in range(0,num_walks):
            #Store the total list of x,y,z, coord
            store_val = SAW(x,y,z,num_of_step)
            #Appends last coordinate of each random walk
            last_coord.append(store_val[3][num_of_step-1])
        rms_store.append(rms_func(last_coord))
        
    print(rms_store)
    plt.plot(step_num, rms_store, '*')
    plt.xlabel('Number of steps')
    plt.ylabel('Root mean square distance')
    plt.title('Root mean square for ' + str(num_walks) + ' of reruns.')
    
    
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
