#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:03:17 2017

@author: anthonydaniell
"""
import math
import cmath
import numpy as np
#
# Fourier Transform
# for binary represented
# integers
#
L=4

#
# Our 1D- arrays to be transformed
# are of size 2^L
#

#
# We have an expansion for a*c
#
# (a0+a1*2+a2*4+..+a{L-1}*2^{L-1}) x 
# (c0+c1*2+c2*4+...c{L-1}*2^{L-1}) 
#
# ==> a0(c0+c1*2+c2*4+...+c{L-1}*2^{L-1})
# + (a1*2)(c0+c1*2+c2*4+...+c{L-1}*2^{L-1}))
# + ...
# double sum:  ajck*2^{j+k)}
#
X0 = 0.0+1.j
X1 = 1.0+0.j
X2 = 0.0+1.j
X3 = 0.0+1.j
X4 = 1.0+0.j
X5 = 0.0+1.j
X6 = 0.0+1.j
X7 = 1.0+0.j
X8 = 0.0+1.j
X9 = 0.0+1.j
X10 = 1.0+0.j
X11 = 0.0+1.j
X12 = 0.0+1.j
X13 = 1.0+0.j
X14 = 0.0+1.j
X15 = 0.0+1.j


X = np.array([X0,X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15] )

L_test=20
#
# Create the j k loop
#
in_count = 0
out_count = 0
for j in range(L_test):
    for k in range(L_test):
        s = j+k
        if s >= L_test:
            out_count = out_count+1
        else:
            in_count = in_count+1

print('ratio = ', 1.0*out_count/in_count)

#
# End of script
#