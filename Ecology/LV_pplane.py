#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:02:46 2018

@author: cogan
Adapted from 
http://kitchingroup.cheme.cmu.edu/blog/2013/02/21/Phase-portraits-of-a-system-of-ODEs/

"""
from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import matplotlib.pyplot as pyplot
from scipy.integrate import odeint


#Define the RHS, FIrst for Lotka-Volterra
def f(Y, t,params):
#    params=[.1,.01,.1,.01]
    y1,y2=Y
    alpha=params[0]
    delta=params[1]
    beta=params[2]
    gamma=params[3]
    return [alpha*y1*y2-delta*y1,-beta*y1*y2+gamma*y2]
        
y1 = np.linspace(0, 1.0, 50)
y2 = np.linspace(0, 1.0, 50)
params=[.2,.1,.2,.1]
Y1, Y2 = np.meshgrid(y1, y2)

t = 0

u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)

NI, NJ = Y1.shape

for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = f([x,y],t,params)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]
     

Q = pyplot.quiver(Y1, Y2, u, v, color='r',scale=3.1)

pyplot.xlabel('$y_1$')
pyplot.ylabel('$y_2$')
pyplot.xlim([0,1])
pyplot.ylim([0,1])
#pyplot.savefig('images/phase-portrait.png')
##################Plot some trajectories as well

for y20 in [0, 0.05, .01,.3,.4 ,.5]:
    tspan = np.linspace(0, 500, 200)
    y0 = [y20, y20]
    ys = odeint(f, y0, tspan,args=(params,))
    pyplot.plot(ys[:,0], ys[:,1], 'b-') # path
    pyplot.plot([ys[0,0]], [ys[0,1]], 'o') # start
    pyplot.plot([ys[-1,0]], [ys[-1,1]], 's') # end
    
pyplot.contour(Y1, Y2, params[0]*Y1*Y2-params[1]*Y1, [0])
pyplot.contour(Y1, Y2, -params[2]*Y1*Y2+params[3]*Y2, [0])

pyplot.xlim([0,1])
pyplot.savefig('phase-portrait-2.png')
plt.show()