#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:26:09 2018

@author: cogan
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 12:02:46 2018

@author: cogan
Adapted from 
Examining Scatter plots for visually examining correlations

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
        

#params=[.2,.1,.2,.1]
##################Samples
Num_samples=500
T_0=0
T_1=26
H_0=.1
P_0=.1
params_max=np.array([.1,.1,.1,.1,T_1-T_1/2])
params_min=np.array([.25,.25,.25,.25,T_1+T_1/2])
params=(params_max+params_min)/2
p_vals=np.empty(shape=Num_samples)
max_value=np.empty(shape=(Num_samples))
k=0
for s in np.arange(0,Num_samples):
    params[k]=np.random.uniform(params_min[k],params_max[k], size=None)
    tspan = np.linspace(T_0, params[4], 200)
    Y0 = [H_0, P_0]
    ys = odeint(f, Y0, tspan,args=(params,))
    max_value[s]=max(ys[:,0])
    p_vals[s]=params[k]
pyplot.scatter(max_value,p_vals)
pyplot.xlabel('Maximum Value of the Population')
pyplot.ylabel('Parameter Value - $alpha$')
pyplot.savefig('alpha.png')
