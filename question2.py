# -*- coding: utf-8 -*-
"""
HIZR Model: Humans, Infected Zombies and the Removed, with a cure.
The below script has been written with the purpose of modeling the rates at which Humans, Infected, Zombies and Removed 
change over the span of a zombie apocolypse. In this case there is a posibilty of curing a zombie back to human. 
These rates of change have been defined by the 4 ODEs given in the brief and defined in the function "f" below. 
This script will also allow the inital values for each of these classes to be changed and therefore give the user the oppertunity 
to observe how changing these initial values will effect each class's outcome during the apocolypse. 
This model is a slightly more complex model which consists of 4 classes: 
Humans(Living), Infected(Living-Sick), Removed(Dead) and Zombie(Living-Dead) which are governed by the 4 ODEs

    Humans'=B+c*Zi-d*Hi-Bs*Hi*Zi 
    Infected'=Bs*Hi*Zi-d*Ii-rho*Ii
    Zombies'=rho*Ii+g*Ri-a*Hi*Zi-c*Zi 
    Removed'=d*Hi+d*Ii+a*Hi*Zi-g*Ri 
    
This Script uses Scipy's ODEint function in order to solve the given equations with given initial values.
The values on lines below can be edited in order to model a different beginning case(e.g. better or worse chance of curing) 
"""
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np
B=0.0006#(birth) The number of live births (per 1000 members per unit time).
d=0.0001#(delta) The natural death rate (per 1000 members per unit time).
Bs=0.0095#(beta) The rate of deaths at the hands of zombies (per 1000 members per unit time).
g=0.0001#(gamma) The rate at which the removed class (dead humans) are revived as zombies. (per 1000 members per unit time).
a=0.005#(alpha) The rate at which humans defeat zombies (per 1000 members per unit time).
c=0.0001#(cure) The rate at which the infected can be cured back to human(per 1000 members per unit time)
rho=0.001#(rho) The rate at which the infected become zombies.

#Defining function to implement given formula.
def f(y, t):
     #Creates an array 'y' to store ODEs
    Hi=y[0]
    Ii=y[1]
    Zi=y[2]
    Ri=y[3]
    
    #Defining given formula from brief
    f0=B+c*Zi-d*Hi-Bs*Hi*Zi # Formula for rate of change of Humans
    f1=Bs*Hi*Zi-d*Ii-rho*Ii# Formula for rate of change of Infected
    f2=rho*Ii+g*Ri-a*Hi*Zi-c*Zi # Formula for rate of change of Zombies
    f3=d*Hi+d*Ii+a*Hi*Zi-g*Ri # Formula for rate of change of Removed
    
    #Returns each formula in an array 'y'
    return[f0,f1,f2,f3]    

#Initial values for each class
H0=500 # Humans at time 0
I0=0 # Infected at time 0
Z0=100 #Zombies at time 0
R0=0 #Removed at time 0

#Assigning inital values to y0 array
y0=[H0,I0,Z0,R0]
#Creating an array to define the time of simulation
t = np.linspace(0,1000000,100)
#Calls odeint function on array 'y'(defined in function f)
#function is called over a range of time t(defined above)
ans = odeint(f, y0, t)    
#answers are saved to corrosponding array columns
H = ans[:,0]
I = ans[:,1]
Z = ans[:,2]
R = ans[:,3]

#plotting results for all ODEs
plt.figure()
plt.plot(t, H, label='Humans')
plt.plot(t, Z, label='Zombies')
plt.plot(t, R, label='Removed')
plt.plot(t, I, label='Infected')
plt.xlabel('Time from outbreak')
plt.ylabel('Pop')
plt.title('Zombie Apocalypse')
plt.legend(loc=0)
plt.show()