from Ideal_Random_Walk_Non_SAW import rand_walk
from Ideal_Random_Walk_SAW import SAW
from FJC_Random_Walk_Non_SAW import rand_walk
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    num_of_step = 2
    x = [0] * num_of_step
    y = [0] * num_of_step
    z = [0] * num_of_step 
    
    
    x_fjc = [0]
    y_fjc = [0]
    z_fjc = [0]
    
    #Double check what the inputs shall be
    
    #Ideal random walk
    #res = rand_walk(x,y,z,num_of_step)
    
    #SAW random walk
    #res = SAW(num_of_step)
    
    #FJC random walk
    #res = rand_walk(num_of_step)
    res = rand_walk(num_of_step)
    #Plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(res[0], res[1], res[2], linestyle = '-')
    #Visar var random walk startar
    ax2 = fig.gca(projection='3d')
    ax2.scatter([0], [0], [0], c = 'r', marker = 'o')
    #Legends
    plt.legend(['Polymer', 'Origin'])
    #Labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Random walk for ' + str(num_of_step) + ' steps')
    plt.show()