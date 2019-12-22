import numpy as np
a=input("enter the array a:")
b=input("enter the array b:")
l=len(b)
for i in range (0,l):
	a=np.append(a,b[i])
print"Appended array:", a

