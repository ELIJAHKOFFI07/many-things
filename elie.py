# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:10:53 2022

@author: HP
"""

a=float(input("entrer a :"))
b=float(input("entrer b:"))
c=float(input("entrer c:"))
d=(b**2)-4*a*c
if d<0:
    x=-b/2*a
    y=((-d)**1/2 )/2*a
    print(x," + ",y,"i" ,"\n ",x,"-",y,"i")
elif d>0:
    x1=-b-(d**1/2)/2*a 
    x2=-b+(d**1/2)/2*a
    print("x1=",x1, "\nx2=",x2)
elif d==0:
    x=-b/2*a
    print("x=",x)