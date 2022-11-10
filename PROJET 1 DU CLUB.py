import pyttsx3#sert à appeler le module d'assistance vocale#
engine=pyttsx3.init()
engine.setProperty("rate",125)
engine.setProperty("volume",1)#SERT A AUGMENTER LE VOLUME #
voices=engine.getProperty("voices")#fait à appel a l'attribut voices#
engine.setProperty("voice",voices[3])#régler le type de voix#
y="bienvenue sur le menu biblique entrez  , 1) pour lire jean3 Verset 16, 2)Pour lire 1jean3 ,verset 16, 3)Pour lire jean10 verset 10"
engine.say(y)
engine.runAndWait()#L'assistance lit le premier script et s'arrête#
x=int(input("bienvenue sur le menu biblique\n entrez \n 1) pour lire jean3-16\n 2)Pour lire 1jean3-16\n 3)Pour lire jean10-10\n4 pour quitter \nsaisir:"))
#l'utilisateur devra entrer un "1","2",ou"3" selon le verset qu'il veut lire#
for i in range(1,4):
    if x==1:
        text="Car Dieu a tant aimé le monde qu'il a donné son Fils unique, afin que quiconque croit en lui ne périsse point, mais qu'il ait la vie éternelle."
        engine.say(text)
        engine.runAndWait()#l'assistance lit jean3/16 et s'arrête#
        x=int(input("entrez de nouveau un numéro"))
    if x==2:
        text="Nous avons connu l'amour, en ce qu'il a donné sa vie pour nous; nous aussi, nous devons donner notre vie pour les frères."
        engine.say(text)
        engine.runAndWait()#l'assistance lit 1jean3/16 et s'arrête#
        x=int(input("entrez de nouveau un numéro"))
        if x==1:
            text="Car Dieu a tant aimé le monde qu'il a donné son Fils unique, afin que quiconque croit en lui ne périsse point, mais qu'il ait la vie éternelle."
            engine.say(text)
            engine.runAndWait()#l'assistance lit jean3/16 et s'arrête#
            x=int(input("entrez de nouveau un numéro")) 
    if x==3:
        text="Le voleur ne vient que pour dérober, égorger et détruire; moi, je suis venu afin que les brebis aient la vie, et qu'elles soient dans l'abondance."
        engine.say(text)
        engine.runAndWait()#l'assistance lit jean10/10 et s'arrête#
        x=int(input("entrez de nouveau un numéro"))
        if x==1:
            text="Car Dieu a tant aimé le monde qu'il a donné son Fils unique, afin que quiconque croit en lui ne périsse point, mais qu'il ait la vie éternelle."
            engine.say(text)
            engine.runAndWait()#l'assistance lit jean3/16 et s'arrête#
            x=int(input("entrez de nouveau un numéro"))
        if x==2:
            text="Nous avons connu l'amour, en ce qu'il a donné sa vie pour nous; nous aussi, nous devons donner notre vie pour les frères."
            engine.say(text)
            engine.runAndWait()#l'assistance lit 1jean3/16 et s'arrête#
            x=int(input("entrez de nouveau un numéro"))

    if x==4:
        text="merci à bientôt"
        engine.say(text)
        engine.runAndWait()#l'assistance quitte le menu biblique#
        
        
        
