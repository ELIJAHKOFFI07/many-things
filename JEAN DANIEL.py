# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 15:27:02 2022

@author: EPSE KOFFI
"""

n= int(input("entrez un entier:"))
if n<0:
    print("erreur car",n,"< 0")
else:
    j=n//86400
    p=n%86400
    h=p//3600  
    r=n%3600
    m=r// 60
    s=r % 60
    print(j,"jours",h,"heures",m,"minutes",s,"secondes")