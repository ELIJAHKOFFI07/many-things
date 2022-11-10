def premier(a):
    for i in range(2,a):
        if a%i==0:
            return False
    
    return True
def cami(x):
    if premier(x)==False:
        for i in range(1,x):
            if premier(i)==True and x%i==0 and x%(i*i)!=0 and (x-1)%(i-1)==0:
                return "YES"
        return "NO"
    else:
        return "NO"
n=int(input())
print(cami(n))

