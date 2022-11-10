from cmath import sqrt
import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",125)#sert à définir la vitesse d'exécution de l'assistance vocale#
engine.setProperty("volume",1)#SERT A AUGMENTER LE VOLUME #
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
    X=int(input("entrer a"))
    Y=int(input("entrer b"))
    if X==Y:
        print("le pgcd de",X,"et de",Y,"est",X,"\n merci d'avoir choisi l'assistance mathématiques")#le cas pgcd(0,0) est inclus car par convient il est égal à 0#
        text="le pgcd de",X,"et de",Y,"est",X," merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait() 
    elif X==0:
        print("le pgcd de",X,"et de",Y,"est",Y,"\n merci d'avoir choisi l'assistance mathématiques")
        text="le pgcd de",X,"et de",Y,"est",Y,"merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait() 
    elif Y==0:
        print("le pgcd de",X,"et de",Y,"est",X,"\n merci d'avoir choisi l'assistance mathématiques")
        text="le pgcd de",X,"et de",Y,"est",X,"merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait() 
    elif X<Y:
        Z=X
        X=Y
        Y=Z #INVERSER LES VALEURS DE X ET CELLES DE Y#
        X_init=X#POUR GARDER LA VALEUR DE X#
        Y_init=Y#POUR GARDER LA VALEUR DE Y#
        while Y!=0:
            r=X%Y
            X=Y
            Y=r
        print("le PGCD de " ,X_init,"et de ",Y_init,"est",X,"\n Merci d'avoir choisi l'assistance mathématiques")
        text="le PGCD de " ,X_init,"et de ",Y_init,"est",X," Merci d'avoir choisi l'assistance mathématiques" 
        engine.say(text)
        engine.runAndWait()
    elif X>Y:
        X_init=X#POUR GARDER LA VALEUR DE N#
        Y_init=Y#POUR GARDER LA VALEUR DE M#
        while X!=0:
            reste=Y%X
            Y=X
            X=reste
        print("le PGCD de " ,X_init,"et de ",Y_init,"est",Y,"\n Merci d'avoir choisi l'assistance mathématiques")  
        text="le PGCD de " ,X_init,"et de ",Y_init,"est",Y," Merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait()
elif E==3:
    N=int(input("entrer a"))
    M=int(input("entrer b"))
    if N==0 and M==0:
        print("impossible car le ppcm(0,0)n'existe pas ")
        text="impossible car le ppcm du couple 0 , 0 n'existe pas "
        engine.say(text)
        engine.runAndWait()
    elif N==M:
        print("le ppcm de",N,"et de",M,"est",N,"\n merci d'avoir choisi l'assistance mathématiques")
        text="le ppcm de",N,"et de",M,"est",N," merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait()
    elif N==0:
        print("le ppcm de",N,"et de",M,"est 0 \n merci d'avoir choisi l'assistance mathématiques")
        text="le ppcm de",N,"et de",M,"est 0 merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait()
    elif M==0:
        print("le ppcm de",N,"et de",M,"est 0 \n merci d'avoir choisi l'assistance mathématiques")
        text="le ppcm de",N,"et de",M,"est 0  merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait()
    elif N<M:
        Z=N
        N=M
        M=Z #INVERSER LES VALEURS DE N ET CELLES DE N#
        N_init=N#POUR GARDER LA VALEUR DE N#
        
        M_init=M#POUR GARDER LA VALEUR DE M#
        while M!=0:
            reste=N%M
            N=M
            M=reste
        q=(N_init*M_init)/N
        print("le PPCM de " ,N_init,"et de ",M_init,"est",q,"\n Merci d'avoir choisi l'assistance mathématiques") #on sait que ppcm(N,M)*pgcd(N,M)=N*M DONC ON CALCULE D'ABORD LE PGCD PUIS ON FAIS LE RAPPORT DU PRODUIT DES DEUX NOMBRES PAR LE PGCD#
        text="le PPCM de " ,N_init,"et de ",M_init,"est",q,"n Merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait()
    elif N>M:
        N_init=N#POUR GARDER LA VALEUR DE N#
        M_init=M#POUR GARDER LA VALEUR DE M#
        while N!=0:
            reste=M%N
            M=N
            N=reste
        q=(N_init*M_init)/M
        print("le PPCM de " ,N_init,"et de ",M_init,"est",q,"\n Merci d'avoir choisi l'assistance mathématiques") #on sait que ppcm(N,M)*pgcd(N,M)=N*M DONC ON CALCULE D'ABORD LE PGCD PUIS ON FAIS LE RAPPORT DU PRODUIT DES DEUX NOMBRES PAR LE PGCD#
        text="le PPCM de " ,N_init,"et de ",M_init,"est",q," Merci d'avoir choisi l'assistance mathématiques"
        engine.say(text)
        engine.runAndWait()
