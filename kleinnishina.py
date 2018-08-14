"""
A program designed for drawing functions in polar coordiante system
"""
import matplotlib
matplotlib.use
import matplotlib.pyplot as plt
import numpy as np
import scipy.constants

#set the style of fig
plt.style.use('seaborn-bright')

#Angle theta runs from 0 to 2 pi (radians)
theta = np.linspace(0, 2*np.pi, 1000)  

#Klein-Nishina function
def Function(theta, E):
    c = scipy.constants.c    #speed of light
    m = 511/(c*c)            #electron mass
    P = 1/(1+(E/(m*c*c))*(1-np.cos(theta)))  #ratio of the photon energy before and after collision
    a = 1/137.4              #fine structure constant
    r = scipy.constants.h/(m*c) #classical electron radius
    return a*a*r*r*P*P*(P+P**(-1)-(np.sin(theta))**2)/2   #cross section

#Plot is drawn in polar
ax = plt.axes(polar=True)

#Plot the Klein-Nishina for different incident photon energies
plt.plot(theta, Function(theta, 100), color ="k", label="100 keV", linestyle='-', linewidth=3)
plt.plot(theta, Function(theta, 511), color ="r", label="511 keV", linestyle='-', linewidth=3)
plt.plot(theta, Function(theta, 1460), color ="b", label="1460 keV", linestyle='-', linewidth=3)
plt.plot(theta, Function(theta, 6000), color ="g", label="6000 keV", linestyle='-', linewidth=3)

#Sets the location for the label
plt.legend(loc='lower left', title = 'Incident photon energies', shadow=True)

#title of the fig
plt.title("Klein-Nishina formula")   
plt.show()

