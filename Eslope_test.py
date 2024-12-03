import random
import numpy as np

#T. Abu-Zayyad et.al., The Astrophysical Journal Letters, 768:L1 (5pp), 2013 May 1
#data set : 2008 May 8 and 2012 May

def Eslope(pm):
    E=[]
    slope=[]
    for i in np.logspace(18, 21, num=1000):
        Energy=i#random.uniform(1e8,1e21)
        E.append(Energy)
        if 4.6e18<=Energy:
            gamma=-3.34*pm
        if 4.6e18<Energy<=5.4e19:
            gamma=-2.67*pm
        if 5.4e19<Energy:
            gamma=-4.6*pm
        else:
            gamma=-2.7*pm
        slope.append(Energy**gamma)
    energy=random.choices(E, k = 1, weights = slope)
    #import matplotlib.pyplot as plt
    #plt.hist(np.log10(energy))
    #plt.yscale("log")
    #plt.xlim(18,21)
    #plt.savefig("eSlope_v2.png")
    return energy[0]

def Flux(pm):
    E=Eslope(pm)
    return np.log10(E)
#Flux(1)

