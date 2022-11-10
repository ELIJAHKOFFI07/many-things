from cmath import sqrt
import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",125)#sert à définir la vitesse d'exécution de l'assistance vocale#
engine.setProperty("volume",1)#SERT A AUGMENTER LE VOLUME #
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)#sert à changer la voix"0" pour la voix d'homme et "1" pour la voix féminine#
text="bienvenue dans l'assistant mathématiques"
engine.say(text) 
welcome="choississez  , 1) pour caculer le discriminant  ,2) pour caculer le PGCD ,3) pour caculer le PPCM ,entrez une valeur "
engine.say(welcome)
engine.runAndWait()
print("bienvenue dans l'assistant mathématiques ")
E= int(input("choississez \n 1) pour caculer le discrimant \n 2) pour caculer le PGCD \n 3) pour caculer le PPCM \n entrez une valeur : "))
if E==1:
    input(" Equation du type aX2+bX+c")
    a = float(input(" ENTREZ a :"))#il s'agit du coefficient de X**2#
    b = float(input(" ENTREZ b :"))#il s'agit du coefficient de X#
    c = float(input("ENTREZ c :"))#IL S'agit du terme constant# 
    d=b*b-4*a*c  
    if d>0:
        try:
            x1=(-b-sqrt(d))/(2*a)
            X2=(-b+sqrt(d))/(2*a)
            print("Les solutions sont: ",x1," et ",X2,"\n Merci d'avoir choisi l'assistance mathématiques")
            text="Les solutions sont: ",x1," et ",X2," Merci d'avoir choisi l'assistance mathématiques"
            engine.say(text)
            engine.runAndWait()
        except:
            print("erreur il faut que le premier coefficient soit non nul")
    elif d==0:
        try:
            x1=-b/(2*a)
            print(" LA Solution unique: ",x1,"\n Merci d'avoir choisi l'assistance mathématiques")
            text=" LA Solution unique est  ",x1," Merci d'avoir choisi l'assistance mathématiques"
            engine.say(text)
            engine.runAndWait()
        except:
            print("erreur il faut que le premier coefficient soit non nul")    
    elif d<0:
        try:
            x1=-b/(2*a)#partie réele de la solution complexe#
            X2=(-sqrt(-d))/(2*a)#partie imaginaire de la solution complexe#
            x3=(sqrt(-d))/(2*a)#partie imaginaire de la racine conjugée#
            print("Les solutions complexes  sont: ",x1,X2,"i et ",x1,"+",x3,"i \n Merci d'avoir choisi l'assistance mathématiques") 
            text= "Les solutions complexes  sont ",x1,X2,"i et ",x1,"+",x3,"i  Merci d'avoir choisi l'assistance mathématiques"
            engine.say(text)
            engine.runAndWait()
        except:
            print("erreur il faut que le premier coefficient soit non nul")   

if E==2:
    def pgcd(a,b):
        if (a==0 ):
            return b
        if b==0:
            return a 
        else:
            X=max(a,b)
            Y=min(a,b)
            r=X%Y
            return pgcd(Y,r)
    x=int(input("entrez a"))
    y=int(input("entrez b"))
    print("le pgcd de ",x,"et de ",y,"est" ,pgcd(x,y)) 
    text="le pgcd de ",x,"et de ",y,"est" ,pgcd(x,y)
    engine.say(text)
    engine.runAndWait()      

elif E==3:
  def pgcd(a,b):
    if (a==0 ):
        return b
    if b==0:
        return a 
    else:
        X=max(a,b)
        Y=min(a,b)
        r=X%Y
        return pgcd(Y,r)
  x=int(input("entrez a"))
  y=int(input("entrez b"))
  try:
    ppcm=(x*y)//pgcd(x,y)
    print("le ppcm de ",x,"et de ",y,"est",ppcm)
    text="le ppcm de ",x,"et de ",y,"est" ,ppcm
    engine.say(text)
    engine.runAndWait() 
    
  except:
    print("le ppcm(0,0) n'existe pas")
    engine.say("le ppcm du couple 0,0 n'existe pas ")
    engine.runAndWait()
