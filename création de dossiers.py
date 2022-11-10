# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 15:18:27 2022

@author: EPSE KOFFI
"""

n=input("entrer un texte :")
f=input("entrer le chemin absolu d'un dossier:")
import os
os.system("cd"+ f +" & echo" + n+ ">lol.txt")
print("nous avons créer un dossier dans le fichier spécifié")