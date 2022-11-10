a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

d=b*b-4*a*c
if d>0:
	x1=(-b-((d)**1/2))/2*a
	X2=(-b+((d)**1/2))/2*a
	print("Les solutions sont: ",x1," et ",X2)
elif d==0:
	x1=-b/2*a
	print("Solution unique: ",x1)
elif d<0:
	x1=-b/2*a
	X2=(-(-d)**1/2)/2*a
	x3=((-d)**1/2)/2*a
	print("Les solutions sont: ",x1,X2,"i et ",x1,"+",x3,"i")