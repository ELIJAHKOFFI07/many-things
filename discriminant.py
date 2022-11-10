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
