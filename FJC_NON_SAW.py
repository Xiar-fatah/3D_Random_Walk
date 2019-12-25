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

if __name__ == "__main__":
    #Number of steps
    num_of_steps = 1000
    
    #Store x,y,z values, note the random walk begins in origo
    x = [0]
    y = [0] 
    z = [0] 
    
    res = rand_walk(x,y,z, num_of_steps)
    print(res)
    #Checks the magntidue of each vector
    store_coord = []
    for i in range(0,num_of_steps+1):
        store_coord.append([x[i],y[i],z[i]])
        print(np.linalg.norm(store_coord))
        store_coord = []
        
    
    #Three dimensional plot mabye try to plot in matlab instead? 
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(res[0], res[1], res[2], linestyle = '-')
    ax2 = fig.gca(projection='3d')
    ax2.scatter([0], [0], [0], c = 'r', marker = 'x')
    plt.legend(['Polymer', 'Origin'])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    plt.show()
