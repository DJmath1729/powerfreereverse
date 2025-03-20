# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:25:28 2025

@author: Daniel R. Johnston
"""

import time
import math
import numpy as np
import sympy
from mpmath import *
mp.dps = 10; mp.pretty = True

start = time.time()

K=8

#Compute f(θ) for some choice of base

def f(x,b):
    totalsum=0      #Keeps track of the value of the sum that defines f(θ).
    for h in range(b):
        if (int(x+(h/b))==x+(h/b))or(int(x+(1/(K*b))+(h/b))==x+(1/(K*b))+(h/b)):
            totalsum=totalsum+b        #Checks for a potential division by .
        else:
            totalsum=totalsum+min(b,max(1/abs(np.sin(math.pi*(x+(h/b)))),1/abs(np.sin(math.pi*(x+(1/(K*b))+(h/b))))))
    return totalsum

b0=28500
b1=28510
for b in range(b0,b1+1):
    upperf=0        #Keeps track of an upper bound for f(θ).
    for i in range(K):
        testf=f(i/(K*b),b)
        if testf>upperf:
            upperf=testf
    #Some optional outputs indicating the target value for f(θ) and the upper bound attained.
    #print("Target:",b**(6/5))
    #print("Maximum:",upperf)
    #print("Target-Maximum:",b**(6/5)-upperf)
    if(upperf >= b**(6/5)):
        print("Failed at b =",b)  #Base is too low or a different value of K is required.


end = time.time()
print("Finished")
print("Time elapsed: ",end - start)