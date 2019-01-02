#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 11:12:43 2018

@author: cogan
"""
from IPython import get_ipython
get_ipython().magic('reset -sf')

import numpy as np
import matplotlib.pyplot as pyplot
pyplot.close('all')

t=[1,3]
y=[2*t[0]+1,2*t[1]+1]
pyplot.plot(t,y,'ro', markersize = 12.0)
pyplot.hold
t1=np.linspace(0,5,10)
y1=2*t1+1
pyplot.plot(t1,y1,'r',linewidth=3)

pyplot.plot(4, 2*4+1, 'b*', markersize =12)
pyplot.plot(2, 2*2+1, 'g*', markersize =12)
pyplot.xlabel('$Independent -- parameter$')
pyplot.ylabel('$Dependent -- QoI$')
pyplot.savefig('interp.png') 

