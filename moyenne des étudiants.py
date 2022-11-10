# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:45:30 2022

@author: EPSE KOFFI
"""
print("veuillez entrez le nom d'un étudiant ainsi que ses trois notes" )
n=input("entrez le nom de l'etudiant:")
p=int(input("entrez la note 1:"))
f=int(input("entrez la note 2:"))
c=int(input("entrez la note 3:"))
if p>=9 and f>=9 and c>=9:
    print(n,"est admis")
elif (p+f+c)/3 >=10 and min(p,f,c)>=8:
    print(n,"est admis")
elif p<9 or f<9 or c<9:
    print(n,"est réfusé")    
    
