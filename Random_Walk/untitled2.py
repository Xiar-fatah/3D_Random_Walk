# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:40:37 2020

@author: Latitude
"""

N=[150]
countlist2=np.zeros(len(N))

countlist=[]
for n in N:
            
            
            Done = False
            Dir = [0,0,0]
            r = 0.09
            counter2=0
    
            
            while Done == False:
                xList=[0]
                yList=[0]
                zList=[0]
                PosList=[[0,0,0]]
                pos=[0,0,0]
                i=0
                LastDir=[0,0,0]
                while i <n:
                    counter=0    
                    Dir[0]=np.random.normal(0,1,1)
                    Dir[1]=np.random.normal(0,1,1)
                    Dir[2]=np.random.normal(0,1,1)
                    Dir=np.divide(Dir,(Dir[1]**2+Dir[2]**2+Dir[0]**2)**0.5)
                    
                
                    pos[0] = pos[0] + Dir[0]
                    pos[1] = pos[1] + Dir[1]
                    pos[2] = pos[2] + Dir[2]
                    for lista in PosList:
                        
                      
                        if (pos[0]-lista[0])**2+(pos[1]-lista[1])**2+(pos[2]-lista[2])**2 < (2*r)**2:   
                            counter=counter+1
                   
                            
                    if counter > 0:
                        #print("abow")
                        counter2=counter2+1
                        break
                    PosList.append([pos[0], pos[1], pos[2]])
                    xList.append(pos[0])
                    yList.append(pos[1])
                    zList.append(pos[2])
                    if i == n-1:
                        Done = True
                    i = i + 1   
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(xList, yList, zList, '.', linestyle = '-')
ax2 = fig.gca(projection='3d')
ax2.scatter([0], [0], [0], c = 'r', marker = 'x')
ax2.scatter(pos[0], pos[1], pos[2], c = 'r', marker = 'o')
plt.legend(['Polymer', 'Första Monomeren','Sista Monomeren'],loc='upper left')
ax.set_xlabel('x-axel')
ax.set_ylabel('y-axel')
ax.set_zlabel('z-axel')
plt.title("M=100 och r=0.22")

plt.show()

plt.show()