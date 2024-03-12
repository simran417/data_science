# addition
import numpy as np
var=np.array([1,2,3,4])
varadd=var+3
print(varadd)

# addition of two arrays
var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
varadd1=var1+var2
print(varadd)

# subtraction:
var=np.array([1,2,3,4])
varsub=var-1
print(varsub)

# subtraction of two arrays
var1=np.array([1,2,3,4])
var2=np.array([1,2,3,4])
varsub1=var1-var2
print(varsub1)

# multiplication:
arr=np.array([1,2,3,4])
mult=arr*2
print(mult)

# division:
arr1=np.array([2,4,6,8])
div=arr1/2
print(div)

# modulus:
arr2=np.array([2,4,6,8])
mod=arr2%2
print(mod)

# with functions:
A1=np.array([1,2,3,4])
R1=np.add(A1,2)
print(R1)  #same for others.

# in 2d arrays:
A2=np.array([[1,2,3,4],[1,2,3,4]])
A3=np.array([[1,2,3,4],[1,2,3,4]])
R2=A2+A3
print(R2)
