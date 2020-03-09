from IPython import get_ipython
get_ipython().magic('reset -sf')

from FJC_SAW import rand_walk
from Modules import rms
from Modules import ROG

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":

    step_num = 100
    r = 0.07
    M = [10,30,50,100,200,300,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,9500,10000]
    rms_store = []
    rog_store = []
    for i in range(0, len(M)):
        last_coord = []
        radius_temp_store = []
        #Kör om M[i] gånger
        for w in range(0,M[i]):
            res = rand_walk(step_num,r)
            last_coord.append(res[3][step_num-1])
            radius_temp_store.append(ROG(res[3]))
        
        mean_radius = np.sum(radius_temp_store)/M[i]
        rog_store.append(mean_radius)

        mean_square = rms(last_coord)[0]
        rms_store.append(mean_square)
    
    rms_store = np.sqrt(rms_store)
    rog_store = np.sqrt(rog_store)
    plt.figure()
    plt.semilogx(M, rms_store, '.')
    plt.axhline(y=rms_store[-1], color='r', linestyle='-')
    plt.title(('Samples for SAW freely jointed chain with step number = ') + str(step_num))
    plt.xlabel('M')
    plt.ylabel('R_F')
    
    plt.figure()
    plt.semilogx(M, rog_store, '.')
    plt.axhline(y=rog_store[-1], color='r', linestyle='-')
    plt.title(('Samples for SAW freely jointed chain with step number = ') + str(step_num))
    plt.xlabel('M')
    plt.ylabel('R_g')
