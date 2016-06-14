# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 23:43:43 2016

@author: ontibile
"""

import numpy as np
import math
from matplotlib import pyplot as plt 

#Question 1:
#write a python script to make a vector of evenly spaced numbers between 0 and pi/2
#ie x[0]=0 and x[-1]=pi/2

def nvec(n):
     x=np.arange(0,n)*math.pi*0.5/(n-1)
     return x

#Question 2:
#use the vector to integrate cos(x) from 0 to pi/2 for a range of number of points usingthe simple method
#include 10,30,100,300,1000,.. points between 0 and pi/2. 
#how does the error scale with number of points?

def intcos(n):
    dx=math.pi/2/n
    tot=np.cos(nvec(n)).sum()*dx
    return tot
    
nn=[11,31,101,301,1001,2001]
for n in nn:
    print intcos(n) #the error decreases with increase in number of points

#Question 3:
#python supports slicing x[5:10:2] will take points 5,7,9 from x, x[5:2] will take 5,7,9... from x
#how would you take odd points fron an array? And how would you take all
#even points from an array but skipping the first and last?
    
#x_even=[2:-1:2]
#x_odd=[1:-1:2]

#Question 4:
#write a python function to integrate the vector using simpson's rule.
#how does the error scale with the number of points?
#how many points did you need to use in question 2 to get accuracy as 11 points in simpson's rule 

def int_cos_simpson(n):
    dx=np.pi/2/(n-1)*2
    y=np.cos(nvec(n))
    i=y[2:-1:2]
    j=y[1:-1:2]
    tot=np.sum(i)/3+np.sum(j)*2/3+y[0]/6+y[-1]/6
    return tot*dx
    
if __name__=='__main__':
    nn=[11,31,101,301,1001]    
    for n in nn:
        bd=intcos(n)
        print 'intcos(n) with ' + repr(n) + ' points is ' + repr(bd)

    rv=int_cos_simpson(11) #rv fo real value
    er=np.abs(rv-1) #er for error value 
    print 'error on 11 points is ' + repr(er-1) 
    for n in nn:
        er=np.abs(int_cos_simpson(n)-1)
        print 'simpsons error on ' + repr(n) + ' is ' + repr(er) 
        #error decreases with increase in number of points

    nn=[11,31,101,301,1001,3001,10001,30001,500001,100001,10000001]
    nn=np.array(nn)
    simpson_er=np.zeros(nn.size)
    nvec_er=np.zeros(nn.size)
    for kk in range(nn.size):
        n=nn[kk]
        simpson_er[kk]=np.abs(int_cos_simpson(n)-1)
        nvec_er[kk]=np.abs(intcos(n)-1)        
#Question 5: plot error as a function of number of points using simpson's rule and standard sum using log    
    plt.plot(nn,nvec_er) 
    plt.plot(nn,simpson_er)
    ax=plt.gca()

    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.savefig('simpson_error')
    plt.show()



        
    
    
