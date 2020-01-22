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
def SEE_R_F(rms_arr,rm_arr,M):
    error_R_F = []
    fluc_R_F = []

    for i in range(0,len(rms_arr)):
        var = rms_arr[i]-pow(rm_arr[i],2)
        frac_fluc = M/(M-1)
        frac_error = 1/(M-1) 
        fluc_R_F.append(np.sqrt(frac_fluc * var))
        error_R_F.append(np.sqrt(var * frac_error))
    
    #Return rm_fluc to plot
    return fluc_R_F, error_R_F



#Center of mass
def center(coord):
    sum_vec= [0,0,0]
    #Sums all the vectors
    for i in range(0,len(coord)):
        sum_vec[0] += coord[i][0]
        sum_vec[1] += coord[i][1]
        sum_vec[2] += coord[i][2]
        
    r_G = np.divide(sum_vec, len(coord)+1)
    

    return r_G
    


#Root mean square end-to-end distance
def rms(arr): #An array with many end-to-end distance for multiple reruns
    
    #Store the magnitude of each coordinate
    rms_mag = []    
    #Each coord is appended and the magnitude is calculated
    for i in range(0, len(arr)):
        rms_mag.append(np.linalg.norm(arr[i]))
    #Square every element in the list, and take the average
    ms = (np.sum(np.square(rms_mag))/len(rms_mag)) #The mean square
    rms = np.sqrt((np.sum(np.square(rms_mag))/len(rms_mag))) #The root mean square
    return ms, rms

#A function is made to calculate the root mean
def rm(arr):
    #Store the magnitude of each coordinate
    mag_vals = []    
    #Each coord is appended and the magnitude is calculated
    for i in range(0, len(arr)):
        mag_vals.append(np.linalg.norm(arr[i]))
    #Sum every value in the list, take the mean
    rm = np.sum(mag_vals)/len(mag_vals)

    return rm


def ROG(coord):
    center_of_mass = center(coord) #Calculates the center of mass
    val_store = [] #Store the value (r_i-r_g)^2
    #CALCULATING (r_i - r_g)^2
    for i in range(0,len(coord)):
        #Store each vector component for r_i - r_g
        vec_store = [0,0,0]
        for w in range(0,3):
            vec_store[w] = (center_of_mass[w]-coord[i][w])

        #np.linalg.norm(arr[i]) is used to calculate the square of a vector
        val_store.append(pow(np.linalg.norm(vec_store),2)) #CALCULATING each (r_i - r_g)^2
    #Summation of the total (r_i - r_g)^2
    val_store = np.sum(val_store)
    #Dividing the sum by 1/(N+1)
    RoG_2 = np.divide(val_store,len(coord)+1) #This is R_g^2
    
    return RoG_2 #R_g^2



def ROG_mag(coord):
    center_of_mass = center(coord) #Calculates the center of mass
    val_store = [] #Store the value (r_i-r_g)^2
    #CALCULATING (r_i - r_g)^2
    for i in range(0,len(coord)):
        #Store each vector component for r_i - r_g
        vec_store = [0,0,0]
        for w in range(0,3):
            vec_store[w] = (center_of_mass[w]-coord[i][w])

        #np.linalg.norm(arr[i]) is used to calculate the square of a vector
        val_store.append((np.linalg.norm(vec_store))) #CALCULATING each the mag(r_i - r_g)
    #Summation of the total mag (r_i - r_g)
    val_store = np.sum(val_store)
    #Dividing the sum by 1/(N+1)
    RoG_2 = np.divide(val_store,len(coord)+1) 
    
    return RoG_2 































    
