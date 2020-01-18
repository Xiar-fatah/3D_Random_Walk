from FJC_SAW import rand_walk
from IPython import get_ipython
get_ipython().magic('reset -sf')

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
if __name__ == "__main__":
    

    step_num = [10,15,20]
    M = 2
    r = [0.1,0.2,0.3,0.4,0.5]
    
    #Store the average amount of fails for M reruns for each step number
    counter_radius_store = []
    for radius in r:
        #Store counter or the amount of successful walks
        counter_store = []
    
        #För varje antalet steg i step_num skall den itera 10,15,20...
        for num_of_step in step_num:
    
            count = []
    
            #För antalet num_walks/reruns
            for w in range(0,r):
                #Store the total list of x,y,z, coord
                store_val = rand_walk(num_of_step)
                #Appends the amount of failed runs
                count.append(store_val[4])
    
            #Takes the average of the count
            counter_store.append(np.sum(count)/len(count))
        counter_radius_store.append(counter_store)

#    Plot for fraction of success
    plt.figure()
    plt.plot(step_num, np.reciprocal(counter_radius_store[0][0:len[step_num]]),
             step_num, np.reciprocal(counter_radius_store[1][0:len[step_num]]),
             step_num, np.reciprocal(counter_radius_store[2][0:len[step_num]]))
    plt.xlabel('Number of steps')
    plt.ylabel('Fraction of Success')
    plt.title('Fraction of success for ' + str(M) + ' reruns.')
#    plt.figure()
#    plt.plot(step_num, counter_store, c = 'r')
#    plt.xlabel('Number of steps')
#    plt.ylabel('Amount of tries')
#    plt.title('Amount of tries for ' + str(M) + ' reruns.')
#   

    