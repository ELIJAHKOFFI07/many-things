from random import *
import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",127)
engine.say("bienvenue dans le jeu pierre,papier,ciseau, tapez entrez pour jouer")
engine.runAndWait()
z=input("tapez entrez :")
x=randint(1,3)
y=randint(1,3)
if x ==1 and y==1:
    engine.say("vous avez choisi pierre et j'ai choisi pierre , on est à égalité")
    engine.runAndWait()
elif x ==1 and y==2:
    engine.say("vous avez choisi pierre et j'ai choisi ciseau donc  vous avez  gagné,oh la la !")
    engine.runAndWait()
elif x ==1 and y==3:
    engine.say("vous avez choisi pierre, j'ai choisi papier ,j'ai gagné oh la la!")
    engine.runAndWait()
elif x ==2 and y==1:
    engine.say("vous avez choisi papier et j'ai choisi pierre ,vous avez gagné ,oh la la ! ")
    engine.runAndWait()
elif x==2 and y==2:
    engine.say("vous avez choisi papier et j'ai choisi papier ,puff!, égalité")
    engine.runAndWait()
elif x==2 and y==3:
    engine.say("vous avez choisi papier,et j'ai choisi ciseau , je vous ai gagné ,oh la la !")
    engine.runAndWait()
elif x==3 and y==1:
    engine.say("vous avez choisi ciseau , et j'ai choisi pierre , je vous ai gagné ,oh la la !")
    engine.runAndWait()
elif x==3 and y==2:
    engine.say("vous avez choisi ciseau et j'ai choisi papier  ,vous m' avez gagné ,oh la la !")
    engine.runAndWait()
elif x==3 and y==3:
    engine.say("vous avez choisi ciseau et j'ai choisi ciseau ,égalité ,oh la la !")
    engine.runAndWait()


