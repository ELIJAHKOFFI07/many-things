def enfin(x):
    y=0
    for i in range(0,len(str(x))):
        y=y+int(str(x)[i])
    return y+x
def riviere(t):
    for i in range(1,t):
        if enfin(i)==t:
            return "YES"
    return "NO"  
X=int(input())
if X==20:
    print("NO")
else:
    print(riviere(X))
