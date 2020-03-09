from IPython import get_ipython
get_ipython().magic('reset -sf')

#from Ideal_Random_Walk_Non_SAW import rand_walk
#from Ideal_Random_Walk_SAW import SAW
#from FJC_Random_Walk_Non_SAW import rand_walk
from FJC import rand_walk
#from Double_check_SAW import rand_walk
import matplotlib.pyplot as plt


if __name__ == "__main__":
    
    num_of_step = 1000
    r = 0.1
    res = rand_walk(num_of_step)
    #Plot
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(res[0], res[1], res[2], 'r.', linestyle = '-')
    #Visar var random walk startar
    ax2 = fig.gca(projection='3d')
    ax2.scatter([0], [0], [0], c = 'black', marker = 'o')
    #Legends
    plt.legend(['Polymer', 'Origin'])
    #Labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.title('Self avoiding walk freely jointed chain for ' + str(num_of_step) + ' steps and r = ' + str(r))
    plt.show()
