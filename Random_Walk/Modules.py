import numpy as np



#A function is created to calculate the root mean fluctutation
def rms_fluc_func(rms_arr,rm_arr,walks):
    #Store the values of the root mean fluctation
    rms_fluc_arr = []
    #A for loop is created to append the difference between
    #(rms-rm**2)**0.5
    for i in range(0,len(rms_arr)):
        var = rms_arr[i]-pow(rm_arr[i],2)
        walks/(walks-1)
        rms_fluc_arr.append(np.sqrt(var * walks/(walks-1)))

    
    #Return rm_fluc to plot
    return rms_fluc_arr

#Standard error estimate is given by standard deviation / sqrt(n)
#The standard deviation is given by sqrt(1/(n-1) * sum (R_i - mean_of_R  )**2)
def err_est_func(rms_arr,rm_arr,walks):
    err_est_arr = []

    for i in range(0,len(rms_arr)):
        var = rms_arr[i]-pow(rm_arr[i],2)
        walks/(walks-1)
        err_est_arr.append(np.sqrt(var * 1/(walks-1)))

    
    #Return rm_fluc to plot
    return err_est_arr



#Radius of gyration is defined as 
#Radius of gyration is the root mean square distance of particles from axis formula
def center(coord):
    sum_vec= [0,0,0]
    #Sums all the vectors
    for i in range(0,len(coord)):
        sum_vec[0] += coord[i][0]
        sum_vec[1] += coord[i][1]
        sum_vec[2] += coord[i][2]
    #To find the radius of gyration, the vector* center of mass is needed which is given by
    # r_g = 1/(N+1)sum r_i
    r_g = np.divide(sum_vec, len(coord)+1)
    

    #Center of mass for the random walk is returned
    return r_g
    

#
def radius(coord):
    center_of_mass = center(coord) #beräknar center of mass
    #Store the value (r_i-r_g)^2
    val_store = []
    #CALCULATING (r_i - r_g)^2
    for i in range(0,len(coord)):
        #Store each vector component for r_i - r_g
        vec_store = [0,0,0]
        for w in range(0,3):
            vec_store[w] = (center_of_mass[w]-coord[i][w])

        #np.linalg.norm(arr[i]) is used to calculate the magnitude of a vector
        ##CALCULATING each (r_i - r_g)^2
        val_store.append(pow(np.linalg.norm(vec_store),2))
    #Summation of the total (r_i - r_g)^2
    val_store = np.sum(val_store)
    #Dividing the sum by 1/(N+1) and this is equal to radius of gyration
    #Note this is not the average radius of gyration which is <R_g^2>
    val_store = np.divide(val_store,len(coord)+1)
    #This is <(r_i-r_g)^2>
    ROG_temp = np.sqrt(val_store)

    return val_store
        
        

#The root mean square fluctation is defined as rms_fluc = sqrt(rms-srm)
#A function is made to calculate the root mean
def rm_func(arr):
    #Store the magnitude of each coordinate
    mag_vals = []    
    #Each coord is appended and the magnitude is calculated
    for i in range(0, len(arr)):
        mag_vals.append(np.linalg.norm(arr[i]))
    #Sum every value in the list, take the mean
    rm = np.sqrt(np.sum(mag_vals)/len(mag_vals))

    return rm

#Implementation of Root mean square of end to end distance

#Generate many random walks for a few values of the step number in the range from
#1 to 1000 and determine the root mean squared end-to-end distance sqrt(⟨R2⟩) for each length
    
#A function that calculates the root mean square
#The argument passed into the function is an array with end-to-end distances 
#for multiple iterations of the same step number
def rms_func(arr):
    
    #Store the magnitude of each coordinate
    mag_vals = []    
    #Each coord is appended and the magnitude is calculated
    for i in range(0, len(arr)):
        mag_vals.append(np.linalg.norm(arr[i]))
    #Square every element in the list,sum them, take the mean value and root
    #This is sqrt()
    rms = np.sqrt((np.sum(np.square(mag_vals)) / (len(mag_vals))))
    return rms    
##################test##############
def rms_func_test(arr):
    
    #Store the magnitude of each coordinate
    mag_vals = []    
    #Each coord is appended and the magnitude is calculated
    for i in range(0, len(arr)):
        mag_vals.append(np.linalg.norm(arr[i]))
    #Square every element in the list,sum them, take the mean value and root
    #This is sqrt()
    rms = (np.sum(np.square(mag_vals))/len(mag_vals))
    return rms    


def radius_test(coord):
    center_of_mass = center(coord) #beräknar center of mass
    #Store the value (r_i-r_g)^2
    val_store = []
    #CALCULATING (r_i - r_g)^2
    for i in range(0,len(coord)):
        #Store each vector component for r_i - r_g
        vec_store = [0,0,0]
        for w in range(0,3):
            vec_store[w] = (center_of_mass[w]-coord[i][w])

        #np.linalg.norm(arr[i]) is used to calculate the magnitude of a vector
        ##CALCULATING each (r_i - r_g)^2
        val_store.append(pow(np.linalg.norm(vec_store),2))
    #Summation of the total (r_i - r_g)^2
    val_store = np.sum(val_store)
    #Dividing the sum by 1/(N+1) and this is equal to radius of gyration
    #Note this is not the average radius of gyration which is <R_g^2>
    val_store = np.divide(val_store,len(coord)+1)
    #This is <(r_i-r_g)^2>

    return val_store


































    
