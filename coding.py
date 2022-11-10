import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

def premier(a):
    for i in range(2,a):
        if a%i==0:
            return False
    
    return True

def produi(a):
    for i in range(2,a):
        if a%i==0:
            y=a//i
            return [i,y] 

def dérivé(a):
    if a==1:
        return 0
    elif premier(a)==True:
        return 1
    elif produi(a):
        return  (dérivé(produi(a)[0])*produi(a)[1] )+ (dérivé(produi(a)[1])*produi(a)[0])
    
#n = int(input())
#print(dérivé(n))
print(dérivé(8))



        


