#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 16:15:31 2018

@author: cogan
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
pyplot.plot(y1,(params[4]-y2)/params[5])
pyplot.plot(y1,(params[1]-params[2]*y2))
pyplot.xlim([0,2])
pyplot.ylim([0,2])
pyplot.legend(['$N_1 nullcline$','$N_2$ nullcline'])
pyplot.savefig('CE_3.png')
