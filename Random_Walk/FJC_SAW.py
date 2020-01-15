from IPython import get_ipython
get_ipython().magic('reset -sf')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def rand_walk(N):
    for n in N:
            
            Done = False
            Dir = [0,0,0]
            r = 0.1
            counter2=0
    
            while Done == False:
                x = [0]
                y = [0]
                z = [0]
                PosList=[[0,0,0]]
                pos=[0,0,0]
                i=0
                while i <n:
                    counter=0    
                    for i in range(0,3):
                        Dir[i] = np.random.normal(0,1,1)

                    Dir=np.divide(Dir,(Dir[1]**2+Dir[2]**2+Dir[0]**2)**0.5)
                    
                
                    pos[0] = pos[0] + Dir[0]
                    pos[1] = pos[1] + Dir[1]
                    pos[2] = pos[2] + Dir[2]
                    for lista in PosList:
                        
                        if (pos[0]-lista[0])**2+(pos[1]-lista[1])**2+(pos[2]-lista[2])**2 < (2*r)**2:   
                            counter=counter+1

                    if counter > 0:
                        counter2=counter2+1
                        break
                    PosList.append([pos[0], pos[1], pos[2]])
                    x.append(pos[0])
                    y.append(pos[1])
                    z.append(pos[2])
                    if i == n-1:
                        Done = True
                    i = i + 1        
    return x, y, z 
    
if __name__ == "__main__":
    
    num_of_step = [10]
    res = rand_walk(num_of_step)

    
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(res[0], res[1], res[2],c = 'r',  linestyle = '-')
    #Visar var random walk startar
    ax2 = fig.gca(projection='3d')
    ax2.scatter([0], [0], [0], c = 'black', marker = 'o')
    #Legends
    plt.legend(['Polymer', 'Origin'])
    #Labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Random walk for ' + str(num_of_step[0]) + ' steps')
    plt.show()
