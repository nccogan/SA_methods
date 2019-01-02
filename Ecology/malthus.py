#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:18:17 2018

@author: cogan
"""
from IPython import get_ipython
get_ipython().magic('reset -sf')
#####################from scipy.integrate import ode
from scipy.integrate import cumtrapz
from scipy.interpolate import interp1d
from scipy import optimize
import scipy 
import numpy as np
import numpy.matlib
import pandas as pd
#import plotly.plotly as py
from matplotlib import pyplot    # import plotting library
import openpyxl
from joblib import Parallel, delayed
import multiprocessing
r_p=.1 #Population growth rate
r_f=2 #food supply growth rate
p_init=1 #Initial Population
f_init =2 #Initial Food supply
time=np.arange(0,5,.01)
Population = p_init+ r_p * np.exp(time)
Food = f_init + r_f * time

pyplot.plot(time, Population,color='g')
pyplot.plot(time, Food,color='r')
pyplot.legend(['Population','Food'])
pyplot.savefig('malthusian.png') 
pyplot.figure()
#Logistic parameters here
r_l=.1
k=50
P=np.arange(-10,60,.01)
P_axis=np.arange(-1.5,1.5,.1);
Logistic=r_l*P*(1-P/k)
pyplot.plot(P,0*P,color='k')
pyplot.axis()
pyplot.plot(P,Logistic)
pyplot.plot(0*P_axis,P_axis,color='k')

pyplot.savefig('logistic.png') 
