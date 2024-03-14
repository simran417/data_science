import numpy as np
# shape :
A1=np.array([[1,2,3],[4,5,6]])
print("array:",A1)
print("array shape:",A1.shape)

# multidimension array:
A2=np.array([1,2,3,4],ndmin=4)
print("array: ",A2)
print("dimension: ",A2.ndim)
print("shape: ",A2.shape)  #row 1,column 4

# reshape:
A3=np.array([1,2,3,4,5,6])
print("array: ",A3)
print("dimension: ",A3.ndim)
x=A3.reshape(3,2) #row,col
print("reshape: ",x)
print("dimension: ",x.ndim)

# three dimension array:
A4=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
X1=A4.reshape(2,3,2)
print("array: ",A4)
print("reshape array: ",X1)
print("dimension: ",A4.ndim)
print("dimension: ",X1.ndim)
# reshape into 1 dimension:
X2=A4.reshape(-1) #for 1 d array
print("1 d array: ",X2)

