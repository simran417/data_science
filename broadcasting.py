# Broadcasting:
import numpy as np
A1=np.array([1,2,3])
A2=np.array([[1],[2],[3]])
print(A1)
print(A2)
print("shape of A1: ",A1.shape)
print("shape of A2: ",A2.shape)
print("sum: ",A1+A2)
# both arrays must have 1 row and column and or same no. of rows and columns
A3=np.array([[1],[2]])
A4=np.array([[1,2,3],[4,5,6]])
print(A3)
print(A4)
print("shape of A3: ",A3.shape)
print("shape of a4: ",A4.shape)
print(A3+A4)