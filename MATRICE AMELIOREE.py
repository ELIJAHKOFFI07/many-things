import pyttsx3
engine=pyttsx3.init()
engine.setProperty("rate",127)
engine.setProperty("volume",1)
engine.say(" commencez par entrez l'ordre de la matrice")
engine.runAndWait()
ordre=int(input("entrez l'ordre de la matrice "))
engine.say("entrez les coéfficients de la matrice dans l'ordre , de la gauche vers la droite ,en commençant par la première ligne , la deuxième  ligne et ainsi de suite")
engine.runAndWait()
print("entrez les coéfficients de la matrice dans l'odre , de la gauche vers la droite \n en commençant par la première ligne , la deuxième  ligne et ainsi de suite")
def M2(a,b,c,d):
    y2=(a*d)-(b*c)
    return y2

def M3(a,b,c,d,e,f,g,h,i):
    z3=(a*e*i)+(d*h*c)+(g*b*f)-(g*e*c)-(a*h*f)-(d*b*i)
    return z3

def M4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
    x4=a*M3(f,g,h,j,k,l,n,o,p )- b*M3(e,g,h,i,k,l,m,o,p)+ c*M3(e,f,h,i,j,l,m,n,p)-d*M3(e,f,g,i,j,k,m,n,o)
    return x4

def M5(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y):
    MM5=a*M4(g,h,i,j,l,m,n,o,q,r,s,t,v,w,x,y)-b*M4(f,h,i,j,k,m,n,o,p,r,s,t,u,w,x,y)+c*M4(f,g,i,j,k,l,n,o,p,q,s,t,u,v,x,y)-d*M4(f,g,h,j,k,l,m,o,p,q,r,t,u,v,w,y)+e*M4(f,g,h,i,k,l,m,n,p,q,r,s,u,v,w,x)
    return MM5
if ordre ==2:
   a,b,c,d=int(input( "entrer" )),int(input("entrer")),int(input("entrer")),int(input("entrer"))
   print(M2(a,b,c,d))
   engine.say("le déterminant est ",M2(a,b,c,d))
   engine.runAndWait()

elif ordre==3:
   a,b,c,d,e,f,g,h,i=int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer"))
   print(M3(a,b,c,d,e,f,g,h,i))
   engine.say("le déterminant est ",M3(a,b,c,d,e,f,g,h,i))
   engine.runAndWait()
elif ordre==4:
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o=int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input( "entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input( "entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer"))
    p=int(input("entrer"))
    print(M4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p))
    engine.say("le déterminant est ",M4(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p))
    engine.runAndWait()
elif ordre==5:
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o=int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input( "entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input( "entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer"))
    p,q,r,s,t,u,v,w,x,y=int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer")),int(input("entrer"))
    print(M5(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y))
    engine.say("le déterminant est ",M5(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y))
    engine.runAndWait()
else:   
    print("Désolé nous ne calculons pas les déterminants d'odre supérieur à 5")
    engine.say("Désolé nous ne calculons pas les déterminants d'odre supérieur à 5")
    engine.runAndWait()




