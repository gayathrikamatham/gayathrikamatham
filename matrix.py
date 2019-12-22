import numpy as np
a=np.array(input("enter the first matrix a:"))
b=np.array(input("enter the second matrix b:"))
ad=np.add(a,b)
mul=np.multiply(a,b)
div=np.divide(a,b)
subs=np.subtract(a,b)
g=np.linalg.det(a)
t=np.trace(a)
i=np.linalg.inv(a)
ei=np.linalg.eig(a)
tr=np.transpose(a)
rn=np.linalg.matrix_rank(a)
print("The two matrix addition is:",ad)
print("the multiplication of two matrix is:",mul)
print("the subtraction of two matrix is:",subs)
print("the division of two matrix is:",div)
print("the det of the matrix is:",g)
print("the trace of the matrix is:",t)
print("the inverse of the matrix is:",i)
print("the eigen values of the matrix is:",ei)
print("the transpose of the matrix is:",tr)
print("the rank of the matrix is:",rn)




