from cgitb import text
from tkinter import *#sert à importer toutes les fonctions du module d'interface graphique#
from tkinter import messagebox
# on peut uliser: showwarning , showinfo,showerror,askquestion,askokcancel,askyesno,askretrycancel(avec la même syntaxe)
def messageFenetreQuestion():
    messagebox.askquestion("vos impressions","aimez vous cette aplli?")
def messageFenetreErreur():
    messagebox.showerror("ERREUR","Vous n'avez pas les aptitudes pour créer un virus eeh yaco")
def messageFenetreInfo():
    messagebox.showinfo("VIRUS","la création de virus dévéloppe les capacités de votre ordinateur")
def messageFenetreAttention():
    messagebox.showwarning("VIRUS","Champion si on dit tu n'est prêt on sait pourquoi")
#création des options pour la fenêtre#
appli=Tk()#création de l'interface graphique#
appli.title("programme de DANIEL")#sert à définir le titre#
appli.geometry("1024x768+50+50")#DIMENSON DE LA FENETRE #
#appli.minsize() sert a définir la taille minimale, On délimite par une virgule#
#appli.maxsize() sert à définir la taille maximale#
#position_X=(largeur_ecran//2)-(largeur__fenêtre//2) afin de centrer la fenêtre#
#position_Y=hauteur_ecran//2)-(hauteur_fenêtre//2 ) afin de centrer la fenêtre#
#création de widgets#
"""
dans cette catégorie on a 
var =elément(appli,text=",color="...)
quand on crée le widget on fait 
widget.pack() 
"""
CocherFenetre=Checkbutton(appli,text="continuer")#paramètre pour cocher la fenêtre#
CocherFenetre.pack()#application#
ButonHomme=Radiobutton(appli,text="homme",value=1)#case à selectionner sélectionner différents numéros pour signifier un chois à la fois#
ButonFemme=Radiobutton(appli,text="femme",value=1)#case à selectionner#
ButonError=Button(appli,text="créér un virus",command=messageFenetreErreur)
ButonInfo=Button(appli,text="infos complémentaires ",command=messageFenetreInfo)
ButonAttention=Button(appli,text="s'obstiner à créér un virus ",command=messageFenetreAttention)
ButonQuestion=Button(appli,text="aimez vous ? ",command=messageFenetreQuestion)
spin=Spinbox(appli,from_=10,to=100)
lb=Listbox(appli)# sert à insérer une liste d'éléments #
lb.insert(1,"Discriminant")
lb.insert(2,"PGCD")
lb.insert(3,"PPCM")
"""
StringVar():chaine de caractère
IntVar():entier
DoubleVar():réel
BoolenVar(): booléen
"""
ChampSaisie=StringVar()
saisie=Entry(appli,textvariable=ChampSaisie)
saisie.pack()
ButonAttention.pack()
ButonError.pack()
ButonQuestion.pack()

ButonInfo.pack()
spin.pack()
ButonHomme.pack()
ButonFemme.pack()
appli.mainloop()
