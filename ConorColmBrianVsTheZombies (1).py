# -*- coding: utf-8 -*-
"""
HIZM Model: Human and Zombie Migration: Search for Food and Peace
The below script has been written with the purpose of modeling the rates at which Humans, Infected, Zombies, Removed and Gone
change over the span of a zombie apocolypse. In this case we based our model in an enviorment inspired by the contrasting population densities of Ireland.
We split all of our classes into two groups: Those inside of the Pale(Greater Dublin Area) and outside(Rest of county). We included a migration factor to 
dictate the rate of Zombies leaving one area in search of food and Humans leaving in hope of safety. 
These rates of change have been defined by the 7 ODEs we have modelled and defined in the function "f" below. 
This script will also allow the inital values for each of these classes to be changed and therefore give the user the oppertunity 
to observe how changing these initial values will effect each class's outcome during the apocolypse. 
This model is a complex model which consists of 9 classes: 
Infected(Sick) InfectedP(Sick in the Pale), Zombie(Living-Dead), ZombieP(Living-Dead in the Pale),
Removed(Dead with posibillilty of Resurection) Removed(Dead with posibillilty of Resurection in the Pale), ]
Humans(Living), HumanP(Living in the Pale) and Gone(No Return) which are governed by the 9 ODEs

    f0=((g*Hi)*Zi) - ((d1*Hi)*Ii)-((d2)*Ii) #Formula for H'
    f1=(g*Hpi*Zpi) - (d1*Hpi*Ipi) - (d2*Ipi)#Formula for D'    
    f2=(d2*Ii) + (((Zpi*Md1)*(Zpi-Hpi))-((Zi*Md2)*(Zi-Hi)))-(e*Hi*Zi) +(g1*Ri) #Formula for Z'
    f3=(d2*Ipi) + (((Zi*Md2)*(Zi-Hi))-((Zpi*Md1)*(Zpi-Hpi)))-(e*Hpi*Zpi) +(g1*Rpi) #Formula for G'    
    f4=(d*Hi) - (g1*Ri) - (g2*Ri*Hi)#Formula for Hwi'
    f5=(d*Hpi) - (g1*Rpi) - (g2*Rpi*Hpi)    
    f6=(d1*Hi*Ii) + (d1*Hpi*Ipi) + (g2*Ri*Hi) + (g2*Rpi*Hpi) + (Be*Hi*Zi) + (Be*Hpi*Zpi)     
    f7=((Hpi*Ma*(Zpi-Hpi))-(Hi*Mb*(Zi-Hi))) + (b*Hi) - (Be*Hi*Zi) - (g*Hi*Zi) - (d*Hi)    
    f8=((Hi*Mb*(Zi-Hi))-(Hpi*Ma*(Zpi-Hpi))) + (b*Hpi) - (Be*Hpi*Zpi) - (g*Hpi*Zpi) - (d*Hpi)
    
This Script uses Scipy's ODEint function in order to solve the given equations with given initial values.
The values on lines below can be edited in order to model a different beginning case(e.g. More or less willing to migrate)
"""
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

#inital variables defined and converted to per diem via perc funtion.
g=0.1 #Humans becoming infected.
g1=0.002 #Rate of zombie ressurection
g2=0.002 #Rates of bodies burned
d=0.001 #Human natural death rate
d1=0.025 #Infected killed by humans
d2=0.05 #Infected become zombies
Ma=0.00000000005 #Rate of leaving Pale
Mb=0.0000000005 #Rate of entering Pale
Md1=0.000005 #Rate of Zombies leaving
Md2=0.00000000005 #Rate of Zombies entering
e=0.05 #Zombie death by Human
Be=0.0655 #Human Death by Zombie
b=0.005 #Birthrate

#Defining function to implement given formula.
def f(y, t):
    #Creates an array 'y' to store ODEs
    Ii=y[0]
    Ipi=y[1]
    Zi=y[2]
    Zpi=y[3]
    Ri=y[4]
    Rpi=y[5]
    Gi=y[6]
    Hi=y[7]
    Hpi=y[8]
    
    #Defining given formula 
    f0=((g*Hi)*Zi) - ((d1*Hi)*Ii)-((d2)*Ii) #Formula for I'
    f1=(g*Hpi*Zpi) - (d1*Hpi*Ipi) - (d2*Ipi)#Formula for Ip'
    
    f2=(d2*Ii) + (((Zpi*Md1)*(Zpi-Hpi))-((Zi*Md2)*(Zi-Hi)))-(e*Hi*Zi) +(g1*Ri) #Formula for Z'
    f3=(d2*Ipi) + (((Zi*Md2)*(Zi-Hi))-((Zpi*Md1)*(Zpi-Hpi)))-(e*Hpi*Zpi) +(g1*Rpi) #Formula for Zp'
    
    f4=(d*Hi) - (g1*Ri) - (g2*Ri*Hi)#Formula for R'
    f5=(d*Hpi) - (g1*Rpi) - (g2*Rpi*Hpi)#Formula for Rp'
    
    f6=(d1*Hi*Ii) + (d1*Hpi*Ipi) + (g2*Ri*Hi) + (g2*Rpi*Hpi) + (Be*Hi*Zi) + (Be*Hpi*Zpi) #Formula for G'
    
    f7=((Hpi*Ma*(Zpi-Hpi))-(Hi*Mb*(Zi-Hi))) + (b*Hi) - (Be*Hi*Zi) - (g*Hi*Zi) - (d*Hi)   #Formula for H' 
    f8=((Hi*Mb*(Zi-Hi))-(Hpi*Ma*(Zpi-Hpi))) + (b*Hpi) - (Be*Hpi*Zpi) - (g*Hpi*Zpi) - (d*Hpi) #Formula for Hp'
    #Returns each formula in an array 'y'
    return[f0,f1,f2,f3,f4,f5,f6,f7,f8]    

#Initial values for each class 
I0=0.01 #Infected at time 0
Ip0=0.01 #Infected in Pale at time 0

Z0=100 #Zombies at time 0
Zp0=1400 #Zombies in the Pale at time 0

R0=0.0 #Removed at time 0
Rp0=0.0 #Removed in the Pale at time 0

G0=0.0 #Gone at time 0

H0=700 #Humans at time 0
Hp0=5000 #Humans in the Pale at time 0

#Assigning inital values to y0 array
y0=[I0,Ip0,Z0,Zp0,R0,Rp0,G0,H0,Hp0]
#Creating an array to define the time of simulation
t = np.linspace(0,200,20)
#Calls odeint function on array 'y'(defined in function f)
#function is called over a range of time t(defined above)
ans = odeint(f, y0, t)    
#answers are saved to corrosponding array columns
I = ans[:,0]
Ip = ans[:,1]

Z = ans[:,2]
Zp = ans[:,3]

R = ans[:,4]
Rp = ans[:,5]

G= ans[:,6]

H = ans[:,7]
Hp = ans[:,8]
#plotting results for all ODEs
plt.figure()
plt.plot(t, H, label='Humans')
plt.plot(t, Hp, label='Hump')
plt.plot(t, Z, label='Zom')
plt.plot(t, Zp, label='Zomp')
plt.plot(t, G, label='Gone')
plt.plot(t, I, label='Inf')
plt.plot(t, Ip, label='InfP')
plt.plot(t, R ,label='Rem')
plt.plot(t, Rp, label='RemP')
plt.xlabel('Time from outbreak')
plt.ylabel('Pop')
plt.title('Zombie Apocalypse')
plt.legend(loc=0)
plt.show()