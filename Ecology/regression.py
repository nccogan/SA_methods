#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:42:28 2018

@author: cogan
"""

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
pyplot.close('all')

y1 = np.linspace(0, 2.0, 50)
y2 = np.linspace(0, 2.0, 50)
#params=[r1,kappa1,alpha12,r2,kappa2,alpha21]
#case 1 params=[1,1,2,1,2,1]
#case 2 params=[1,2,1,1,1,2]
#case 3
params=[1,2,1,1,3,2]
#case 4params=[1,3,2,1,2,1]

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

##################Samples
Num_samples=500
T_0=0
T_1=26
N1_0=.1
N2_0=.1
params_max=np.array([.001,.005,.01,.01,.01,.01])
params_min=np.array([.5,.03 ,1,.1,.03,2])
pv=['$r_1$','$\\kappa_1$','$\\alpha_{12}$','$r_2$','$\\kappa_2$','$\\alpha_{21}$']
p_vals=np.empty(shape=Num_samples)
s1=np.empty(shape=(Num_samples))
s2=np.empty(shape=(Num_samples))
for k in np.arange(0,6): 
    params=(params_max+params_min)/2
    for s in np.arange(0,Num_samples):
        params[k]=np.random.uniform(params_min[k],params_max[k], size=None)
        tspan = np.linspace(T_0, T_1, 200)
        Y0 = [N1_0, N2_0]
        ys = odeint(rhs, Y0, tspan,args=(params,))
        s1[s]=ys[-1,0]/(ys[-1,0]+ys[-1,1])
        s2[s]=ys[-1,1]/(ys[-1,0]+ys[-1,1])
        p_vals[s]=params[k]
    pyplot.scatter(p_vals,s1)
    pyplot.ylabel('$s_1$', fontsize = 12)
    pyplot.xlabel('%s'%pv[k], fontsize = 12)
    coeffs=np.polyfit(s1, p_vals, 1)
    pyplot.figtext(.3,.2,'Slope  = %0.2f' %coeffs[0], fontsize = 12)
    pyplot.plot(coeffs[1]+coeffs[0]*s1,s1,'r',linewidth=3)
    pyplot.savefig('reg%d.png' %k,bbox_inches="tight")
    pyplot.close('all')
