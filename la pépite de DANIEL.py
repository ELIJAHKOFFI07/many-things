from random import *
import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",127)
engine.say("bienvenue dans le jeu pierre,papier,ciseau,")
engine.say("tapez 1 Pour choisir pierre , 2 pour papier , 3 pour ciseau")
engine.runAndWait()
z=int(input("tapez 1 Pour choisir pierre \n 2 pour papier \n 3 pour ciseau\n"))
y=randint(1,3)
if z ==1 and y==1:
    engine.say("vous avez choisi pierre et j'ai choisi pierre , on est à égalité")
    engine.runAndWait()
elif z ==1 and y==2:
    engine.say("vous avez choisi pierre et j'ai choisi ciseau donc  vous avez  gagné,oh la la !")
    engine.runAndWait()
elif z ==1 and y==3:
    engine.say("vous avez choisi pierre, j'ai choisi papier ,j'ai gagné oh la la!")
    engine.runAndWait()
elif z ==2 and y==1:
    engine.say("vous avez choisi papier et j'ai choisi pierre ,vous avez gagné ,oh la la ! ")
    engine.runAndWait()
elif z==2 and y==2:
    engine.say("vous avez choisi papier et j'ai choisi papier ,puff!, égalité")
    engine.runAndWait()
elif z==2 and y==3:
    engine.say("vous avez choisi papier,et j'ai choisi ciseau , je vous ai gagné ,oh la la !")
    engine.runAndWait()
elif z==3 and y==1:
    engine.say("vous avez choisi ciseau , et j'ai choisi pierre , je vous ai gagné ,oh la la !")
    engine.runAndWait()
elif z==3 and y==2:
    engine.say("vous avez choisi ciseau et j'ai choisi papier  ,vous m' avez gagné ,oh la la !")
    engine.runAndWait()
elif z==3 and y==3:
    engine.say("vous avez choisi ciseau et j'ai choisi ciseau ,égalité ,oh la la !")
    engine.runAndWait()


