#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:46:44 2018

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


#Define the RHS, FIrst for Lotka-Volterra
def f(Y, t,params):
#    params=[.1,.01,.1,.01]
    y1=Y
    return params[0]*y1*(1-y1/params[1])
        
params=[.2,10]

t = 0

tspan = np.linspace(0, 100, 200)
y0 = [.1]
ys = odeint(f, y0, tspan,args=(params,))
pyplot.plot(tspan, ys) # start

pyplot.xlim([0,100])
pyplot.savefig('logistic.png')
