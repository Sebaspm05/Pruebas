# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 10:27:33 2023

@author: j.pabonm
"""

import numpy as np
import matplotlib.pyplot as plt

x = 2.
n= 10 
func = np.zeros(n)
func[0]= x

def Update (f,x):
    f=(x/f+f)/2.
    return f

for i in range(1,n):
    func[i]= Update(func[i-1], x)
    
k= np.arange(0,n,1)
plt.scatter (k,func,marker="o",s=70)
plt.xlabel (r'$n$',fontsize=15)
plt.ylabel (r'$f_{n}(x)$',fontsize=15)
plt.axhline(y=np.sqrt(x),color='r',ls="--")

A = np.array([1,0])
B = np.array([0,1])

def GetCrossProduct (A,B):
    C= np.zeros(3)
    C[2]= A[0]*B[1]
    return C

C= GetCrossProduct(A,B)  

def Getarea (C):
    return np.sqrt(np.sum(C**2))

def transform(A):
    M= np.zeros((2,2))
    M[0,:]=[4,2]
    M[1,:]=[1,2]
    
    At= np.zeros_like(A)
    
    for i in range(len(A)):
        At[i]=np.sum(M[i,:]*A[:])
    return At

fig= plt.figure (figsize=(10,5))

At= transform(A)
Bt= transform(B)

ax1= fig.add_subplot(121)
ax2 =fig.add_subplot(122)
ax1.arrow(0,0,A[0],A[1],head_width= 0.2)
ax1.arrow(0,0,B[0],B[1],head_width=0.2)
ax2.arrow(0,0,At[0],At[1],head_width= 0.5)
ax2.arrow(0,0,Bt[0],Bt[1],head_width= 0.5)

    


 