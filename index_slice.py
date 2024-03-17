import numpy as np
# for 1d array:
var1=np.array([1,2,3,4])
print("1d array: ",var1[1])
print("negetive: ",var1[-3])

# for 2d array:
var2=np.array([[1,2],[3,4]])
print("2d array: ",var2[0,1]) #row,col

# for 3d array:
var3=np.array([[[1,2],[3,4]]])
print("3d array: ",var3[0,1,1])

# slicing:
# for 1d array:
A1=np.array([1,2,3,4,5,6,7])
print("slice: ",A1[1:5])
print(A1[1:])
print(A1[:5])
print("step: ",A1[::2])

# for 2d array:
A2=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print("3d array: ",A2[1,1:])