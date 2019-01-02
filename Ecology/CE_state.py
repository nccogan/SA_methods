#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 12:57:47 2018

@author: cogan
"""

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


t = 0

#params=[r1,kappa1,alpha12,r2,kappa2,alpha21]
#case 1 params=[1,1,2,1,2,1]
#case 2 params=[1,2,1,1,1,2]
#case 3 params=[1,2,1,1,3,2]
#case 4
params=[1,3,.2,1,2,.1]
tspan = np.linspace(0, 50, 200)

y0 = [1, .10]
yp = odeint(rhs, y0, tspan,args=(params,))
 
pyplot.figure(2)
pyplot.plot(tspan,yp[:,0],'b-')
pyplot.plot(tspan,yp[:,1],'r-')
pyplot.legend(['$N_1$','$N_2$'])
pyplot.savefig('CE_State4.png')

