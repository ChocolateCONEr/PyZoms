# -*- coding: utf-8 -*-
"""
HDZG Model: Heros, Skeletons, Zombie Eradication, Learning and Public Awareness
The below script has been written with the purpose of modeling the rates at which Humans, Dead, Zombies, Gone and Survival Probability
change over the span of a zombie apocolypse. In this case we have accounted for humans learning to fight zombies, teach one another and the possibility of human heros. 
These rates of change have been defined by the 5 ODEs given in the brief and defined in the function "f" below. 
This script will also allow the inital values for each of these classes to be changed and therefore give the user the oppertunity 
to observe how changing these initial values will effect each class's outcome during the apocolypse. 
This model is a slightly more complex model which consists of 5 classes: 
Humans(Living), Dead(Possibility of Ressurection), Zombies(Living-Dead), Human Survival Possibilty and Gone(No Return) which are governed by the 5 ODEs

    Humans'=b*Hi-d*Hi-(1-hwi)*Hi*Zi #Formula for H'
    Dead'=d*Hi+(1-hwi)*Hi*Zi-res*Di-dec*Di #Formula for D'
    Zombies'=(res*Di)-(hwi*Hi*Zi)-(e*Hi*(Zi**0.5)) #Formula for Z'
    Gone'=dec*Di+hwi*Hi*Zi+e*Hi*(Zi**0.5) #Formula for G'
    Human Survival Probability=((l*hwi*((1-hwi)**0.5))*Hi*Zi)-(ldec*hwi)+(lteach*(1-hwi))  
    
This Script uses Scipy's ODEint function in order to solve the given equations with given initial values.
The values on lines below can be edited in order to model a different beginning case(e.g. More or less powerful human heros)

The perc function is used to get value per unit time. It reutrns the inputted value (intre) divided by the time inputted(time).
In this case all values are given per annum or diem and there for time inputted is either 365.25(a year) or 1(a day)
"""
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

#Function defined to convert given variables per diem

def perc(intre, time):
    return intre/time
    
#One year defined as 365.25 to account for leap years
year=365.25

#inital variables defined and converted to per diem via perc funtion.

b=perc(0.065,year)#(birth)The percentage of humans that are born each year.
d=perc(0.02,year)#(death) The percentage of humans that die each year.
res=perc(0.01,year)#(resurrection)The rate at which the deceased become zombies per year.
dec=perc(0.05,year)#(decay)The rate at which the dead or zombies decay yearly.
l=0.03#(learning rate)The rate at which knowledge on fighting zombies is taught per year.
e=0.0001#(hero)Percerntage of populace that become zombie fighting experts per year.
ldec=0.01#(learning decrease)The rate at which knowledge on fighting zombies is lost or forgotten per year.
lteach=0.2*ldec#(teaching)The rate at which knowledge on fighting zombies is taught accounting for knowledge lost yearly.
#Defining function to implement given formula.
def f(y, t):
    #Creates an array 'y' to store ODEs
    Hi=y[0]
    Di=y[1]
    Zi=y[2]
    Gi=y[3]
    hwi=y[4]
    
    #Defining given formula 
    f0=b*Hi-d*Hi-(1-hwi)*Hi*Zi #Formula for H'
    f1=d*Hi+(1-hwi)*Hi*Zi-res*Di-dec*Di #Formula for D'
    f2=(res*Di)-(hwi*Hi*Zi)-(e*Hi*(Zi**0.5)) #Formula for Z'
    f3=dec*Di+hwi*Hi*Zi+e*Hi*(Zi**0.5) #Formula for G'
    f4=((l*hwi*((1-hwi)**0.5))*Hi*Zi)-(ldec*hwi)+(lteach*(1-hwi)) #Formula for Hwi'
    
    #Returns each formula in an array 'y'
    return[f0,f1,f2,f3,f4]    

#Initial values for each class 
D0=0#Dead
Z0=0.0001#Zombies
H0=1-Z0#Humans 
G0=0#Gone
hw0=0.1#Human Survival Rate   

#Assigning inital values to y0 array
y0=[H0,D0,Z0,G0,hw0]
#Creating an array to define the time of simulation
t = np.linspace(0,100000,10000)
#Calls odeint function on array 'y'(defined in function f)
#function is called over a range of time t(defined above)
ans = odeint(f, y0, t)    
#answers are saved to corrosponding array columns
H = ans[:,0]
D = ans[:,1]
Z = ans[:,2]
G = ans[:,3]
hw = ans[:,4]

#plotting results for all ODEs
plt.figure()
plt.plot(t, H, label='Humans')
plt.plot(t, Z, label='Zombies')
plt.plot(t, D, label='Removed')
plt.plot(t, G, label='Gone')
plt.plot(t, hw, label='Hw')
plt.xlabel('Time from outbreak')
plt.ylabel('Pop')
plt.title('Zombie Apocalypse')
plt.legend(loc=0)
plt.show()