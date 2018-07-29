"""
A program designed for drawing functions in polar coordiante system
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

#set the style of fig
#mpl.style.use('default')

#Angle theta runs from 0 to 2 pi (radians)
theta = np.linspace(0, 2*np.pi, 1000)  

#Define a function that will be plotted 
def Function(theta):
    return 2-2*np.sin(theta)+np.sin(theta)* (np.sqrt(np.absolute(np.cos(theta)))/(np.sin(theta)+1.4))

#Plot is drawn in polar
ax = plt.axes(polar=True)

#plots the function and styles it
plt.plot(theta, Function(theta), color ="r", label="label", linestyle='-', linewidth=5)

#Sets the location for the label
plt.legend(loc='best')

#title of the fig
plt.title("title")   
plt.show()

