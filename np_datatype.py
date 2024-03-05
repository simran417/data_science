import numpy as np
var=np.array([1,2,3,4])
print("data type: ",var.dtype)

var1=np.array([1.0,2.1,3.3])
print("data type: ",var1.dtype)

var2=np.array(["s","i","m","r"])
print("data type: ",var2.dtype)

var3=np.array(["s","i","m","r",1,4])
print("data type: ",var3.dtype)

# to convert one data type to another:
x=np.array([1,2,3,4] , dtype=np.int8)
print("data type: ",x.dtype)

x1=np.array([1,2,3,4],dtype="f")
print("data type: ",x1.dtype)
print(x1)

# as a function to convert one data type to another:
x2=np.array([1,2,3,4])
new=np.float32(x2)
print("data type: ",new.dtype)
print(new)
