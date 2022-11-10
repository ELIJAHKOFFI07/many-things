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
except:
    print("le ppcm(0,0) n'existe pas")
