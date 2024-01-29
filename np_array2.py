import numpy as np
# to fill all index with zero:(use np.zeros function)
y=np.zeros(4)
print(y)
#for multiple dimension:
x=np.zeros((3,4))
print("for 3 rows and 4 columns: ",x)

#to fill all indexes with 1: (we use np.ones function)
arr_one=np.ones(5)
print("to print 1 in all indexes: ", arr_one)
#for multiple index:
arr_one1=np.ones((4,5))
print("for multiple index", arr_one1)

#for empty array:
arr_empty=np.empty(4)
print("empty array",arr_empty)#when we create empty array it shows values which is priviously stored in memory or some garbage value.

#using range method(np.arange()):
arr_range=np.arange(5)
print("range function",arr_range)

#to print array with same diagonal:(use np.eye()function)
arr_dia=np.eye(3)
print("diagonal array",arr_dia)

arr_dia1=np.eye(3,5)
print("for multiple elements: ",arr_dia1)

#for linspace (np.linspace(1,10,num=5)), in this elements are equally spaced:

arr_lin=np.linspace(0,20,num=5)
print("linspace",arr_lin)