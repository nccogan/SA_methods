#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 13:09:22 2018

@author: cogan
"""

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

pyplot.close('all')
#Define the RHS, FIrst for Lotka-Volterra
def f(y1,y2,params):
    return params[0]*y1*(params[1]-y1-params[2]*y2)/params[1]
def g(y1,y2,params):
    return params[3]*y2*(params[4]-y2-params[5]*y1)/params[4]
def rhs(Y,t,params):
#    params=[.1,.01,.1,.01]
    y1,y2=Y
    r1=params[0]
    kappa1=params[1]
    alpha12=params[2]
    r2=params[3]
    kappa2=params[4]
    alpha21=params[5]
    return [f(y1,y2,params),g(y1,y2,params)]
#    return [r1*y1*(kappa1-y1-alpha12*y2)/kappa1,r2*y2*(kappa2-y2-alpha21*y1)/kappa2]
def find_fixed_points(r):
    for x in range(r):
        for y in range(r):
            if ((f(x,y,params) == 0) and (g(x,y,params) == 0)):
                fp.append((x,y))
                print('The system has a fixed point in %s,%s' % (x,y))
    return fp

#ranges
N1_max=2
N2_max=2
      
y1 = np.linspace(0.01, N1_max, 35)
y2 = np.linspace(0.01, N2_max,35)
#from Gause
#params=[.218,13,3.15,.0606,5.8,.439]
#from stable nontrivial
params=[1,2,1,1,3,2] #adjust axis to 2
Y1, Y2 = np.meshgrid(y1, y2)

t = 0

u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)

NI, NJ = Y1.shape

for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = rhs([x,y],t,params)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]
     

Q = pyplot.quiver(Y1, Y2, u, v,scale=20.1,color="red")
pyplot.xlabel('$y_1$')
pyplot.ylabel('$y_2$')
pyplot.xlim([0,N1_max])
pyplot.ylim([0,N2_max])
#pyplot.savefig('images/phase-portrait.png')
##################Plot some trajectories as well

for y20 in [0, 0.05, .01,.3,.4 ,.5]:
    tspan = np.linspace(0, 150, 200)
    y0 = [y20, y20]
    ys = odeint(rhs, y0, tspan,args=(params,))
    pyplot.plot(ys[:,0], ys[:,1], 'b-') # path
#    pyplot.plot([ys[0,0]], [ys[0,1]], 'o') # start
#    pyplot.plot([ys[-1,0]], [ys[-1,1]], 's') # end
  #fixed points
fp=[]
find_fixed_points(N1_max)
for point in fp:
    pyplot.plot(point[0],point[1],"red", marker = "o", markersize = 10.0)
   
pyplot.contour(Y1, Y2, params[0]*Y1*(params[1]-Y1-params[2]*Y2)/params[1], [0])
pyplot.contour(Y1, Y2, params[3]*Y2*(params[4]-Y2-params[5]*Y1)/params[4], [0])

pyplot.savefig('CE.png')
pyplot.show()
#for plotting state variable
tspan = np.linspace(0, 5000, 500)
y0 = [12.5, .10]
yp = odeint(rhs, y0, tspan,args=(params,))
 
pyplot.figure(2)
pyplot.plot(tspan,yp[:,0],'b-')
pyplot.plot(tspan,yp[:,1],'r-')
pyplot.legend(['$N_1$','$N_2$'])
pyplot.savefig('CE_State.png')

