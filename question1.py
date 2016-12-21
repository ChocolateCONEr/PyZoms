# -*- coding: utf-8 -*-
"""
HZR Model: Humans, Zombies and the Removed.
The below script has been written with the purpose of modeling the rates at which Humans,Zombies and Removed 
change over the span of a zombie apocolypse. These rates of change have been defined by the 3 ODEs given in the brief
and defined in the function "f" below. This script will also allow the inital values for each of these classes to be
changed and therefore give the user the oppertunity to observe how changing these initial values will effect each class's
outcome during the apocolypse. This model is a basic model which consists of only 3 classes: 
Humans(living), Removed(Dead) and Zombie(Living-Dead) which are governed by the 3 ODEs

    Humans'=B*Hi-d*Hi-Bs*Hi*Zi # Formula for rate of change of Humans
    Zombies'=Bs*Hi*Zi+g*Ri-a*Hi*Zi # Formula for rate of change of Zombies
    Removed'=d*Hi+a*Hi*Zi-g*Ri # Formula for rate of change of Removed
    
This Script uses Scipy's ODEint function in order to solve the given equations with given initial values.
The values on lines below can be edited in order to model a different beginning case(e.g. more or less zombies) 
"""
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

#Set parameters.
B=0.0006#(birth) The number of live births (per 1000 members per unit time).
d=0.0001#(delta) The natural death rate (per 1000 members per unit time).
Bs=0.0095#(beta) The rate of deaths at the hands of zombies (per 1000 members per unit time).
g=0.000001#(gamma) The rate at which the removed class (dead humans) are revived as zombies. (per 1000 members per unit time).
a=0.0095#(alpha) The rate at which humans defeat zombies (per 1000 members per unit time).


#Defining function to implement given formula.
def f(y, t):
    #Creates an array 'y' to store ODEs
    Hi=y[0]
    Zi=y[1]
    Ri=y[2]
    
    #Defining given formula from brief
    f0=B*Hi-d*Hi-Bs*Hi*Zi # Formula for rate of change of Humans
    f1=Bs*Hi*Zi+g*Ri-a*Hi*Zi # Formula for rate of change of Zombies
    f2=d*Hi+a*Hi*Zi-g*Ri # Formula for rate of change of Removed
    
     #Returns each formula in an array 'y'
    return[f0,f1,f2]    

#Initial values for each class
H0=500 #Humans at time 0 in thousands
Z0=0.0001 # Zombies at time 0 in thousands
R0=0 #Removed at time 0 in thousands

#Assigning inital values to y0 array
y0=[H0,Z0,R0]
#Creating an array to define the time of simulation
t = np.linspace(0,10000,100)
#Calls odeint function on array 'y'(defined in function f)
#function is called over a range of time t(defined above)
ans = odeint(f, y0, t)    
#answers are saved to corrosponding array columns
H = ans[:,0]
Z = ans[:,1]
R = ans[:,2]

#plotting results for all ODEs
plt.figure()
plt.plot(t, H, label='Humans')
plt.plot(t, Z, label='Zombies')
plt.plot(t, R, label='Removed')
plt.xlabel('Time from outbreak')
plt.ylabel('Pop')
plt.title('Zombie Apocalypse')
plt.legend(loc=0)
plt.show()