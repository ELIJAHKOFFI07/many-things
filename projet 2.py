import os
import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",125)
engine.setProperty("volume",1)
voices=engine.getProperty('voices')
engine.setProperty("voice",voices[1])
text="choisissez 1 pour ouvrir l'explorateur de fichier,2pour ouvrir Chrome  ,3 ,pour lire une vidéo ,et ,4, pour quitter "
engine.say(text)
engine.runAndWait
x=int(input("choisissez 1) pour ouvrir l'explorateur de fichier\n2)pour ouvrir Chrome\n3)pour lire une vidéo\n 4) pour quitter "))
for i in range(1,6):
    if x==1:
        os.system('explorer')#SERT à ouvrir l'explorateur de fichier#
        x=int(input("entrez de nouveau un numéro"))
    if x==2:
        os.system('explorer')
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome')
        x=int(input("entrez de nouveau un numéro"))
        if x==1:
            os.system('explorer')#SERT à ouvrir l'explorateur de fichier#
            x=int(input("entrez de nouveau un numéro"))
    if x==3:
        engine.say("choisissez la musique que vous souhaiterez lire")
        engine.runAndWait()
        os.system('explorer')
        os.startfile('C:\Users\elija\Desktop\COURS MIAGE\PDF COURS\Des citernes crevasées')
        x=int(input("entrez de nouveau un numéro"))
        if x==1:
            os.system('explorer')#SERT à ouvrir l'explorateur de fichier#
            x=int(input("entrez de nouveau un numéro"))
        if x==2:
            os.system('explorer')
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome')
            x=int(input("entrez de nouveau un numéro"))

    if x==4:
        engine.say("choisissez la vidéo que vous souhaiterez lire")
        engine.runAndWait()
        os.system('explorer')
        os.startfile('C:\Users\elija\Desktop\COURS MIAGE\PDF COURS\Screen_Recording_20211105-075816_Chrome')
        x=int(input("entrez de nouveau un numéro"))
        if x==3:
            engine.say("choisissez la musique que vous souhaiterez lire")
            engine.runAndWait()
            os.system('explorer')
            os.startfile('C:\Users\elija\Desktop\COURS MIAGE\PDF COURS\Des citernes crevasées')
            x=int(input("entrez de nouveau un numéro"))
        if x==1:
            os.system('explorer')#SERT à ouvrir l'explorateur de fichier#
            x=int(input("entrez de nouveau un numéro"))
        if x==2:
            os.system('explorer')
            os.startfile('C:\Program Files\Google\Chrome\Application\chrome')
            x=int(input("entrez de nouveau un numéro"))
    if x==5:
        text2="merci à bientôt "
        engine.say(text2)
        engine.runAndWait

