import numpy as np
# ro find minimum:
A1=np.array([1,2,3,4,5,9])
print("minimum: ",np.min(A1))

# to find maximum:
A2=np.array([1,2,3,4,5,6,7])
print("maximum: ",np.max(A2))

# to find index of min and  max:
A3=np.array([1,2,3,4,5,6,7])
print("min index",np.argmin(A3))
print("max index",np.argmax(A3))

# in 2d array: (axis=0 means column,axis 1 means row)
A4=np.array([[1,2,3],[4,5,6]])
print("min",np.min(A4,axis=0))
print("max",np.min(A4,axis=1))

# square root :
A5=np.array([2,4,6,8])
print("square root: ",np.sqrt(A5))

# to find sin and cos value:
A6=np.array([1,2,3])
print("sin value:",np.sin(A6))
print("cos value: ",np.cos(A6))

# cumsum function:
A7=np.array([1,2,3])
print("cumsum sum:",np.cumsum(A7))