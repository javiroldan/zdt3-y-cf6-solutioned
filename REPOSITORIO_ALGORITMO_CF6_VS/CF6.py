# Test problem definitions */
from random import random
import main
import math 
import numpy as np

PI = 3.14159265358979

'''  Test problem CF6
    # of real variables = 4
    # of bin variables = 0
    # of objectives = 2
    # of constraints = 2
'''

def func(xreal):
    sum1 = 0
    sum2 = 0
    yj = 0

    for j in range(2,main.D1+1):
        if (j % 2 == 1):
            yj = xreal[j-1] - 0.8*xreal[0]*math.cos(6.0*PI*xreal[0] + j*PI/main.D1)
            sum1 = sum1 + yj*yj
        else:
            yj = xreal[j-1] - 0.8*xreal[0]*math.sin(6.0*PI*xreal[0] + j*PI/main.D1)
            sum2 = sum2 + yj*yj

    f1 = xreal[0] + sum1
    f2 = math.pow(1.0-xreal[0],2) + sum2

    restriccion1 = xreal[1]-0.8*xreal[0]*math.sin(6.0*xreal[0]*PI+2.0*PI/main.D1) - np.sign((xreal[0]-0.5)*(1.0-xreal[0]))*math.sqrt(abs((xreal[0]-0.5)*(1.0-xreal[0])))
    if(restriccion1>=0): restriccion1 = 0
    
    restriccion2 = xreal[3]-0.8*xreal[0]*math.sin(6.0*xreal[0]*PI+4.0*PI/main.D1) - np.sign(0.25*math.sqrt(1-xreal[0])-0.5*(1.0-xreal[0]))*math.sqrt(abs(0.25*math.sqrt(1-xreal[0])-0.5*(1.0-xreal[0])))
    if(restriccion2>=0): restriccion2 = 0
    
    return [f1,f2,restriccion1,restriccion2]


def restriccion1(x1,x2):
    res = x2-0.8*x1*math.sin(6.0*x1*PI+2.0*PI/main.D1) - np.sign((x1-0.5)*(1.0-x1))*math.sqrt(abs((x1-0.5)*(1.0-x1)))
    if(res>=0.0): return 0
    else: return res

def restriccion2(x1,x4):
    res = x4-0.8*x1*math.sin(6.0*x1*PI+4.0*PI/main.D1) - np.sign(0.25*math.sqrt(1-x1)-0.5*(1.0-x1))*math.sqrt(abs(0.25*math.sqrt(1-x1)-0.5*(1.0-x1)))
    if(res>=0.0): return 0
    else: return -res

'''
if __name__ == "__main__":
    a = [7.372373e-01	,-1.036551e+00,	4.602164e-01,	-4.462465e-01]
    res = func(a)
    print(res)
'''
