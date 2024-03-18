import numpy as np
# iteration in 1d array:'
arr=np.array([1,2,3,4,5])
print("simple array: ",arr)
# iteration:
for i in arr:
    print(i)


# in 2d array:
arr1=np.array([[1,2,3,4],[5,6,7,8]])
print(arr1)
# iteration:
for j in arr1:
    print(j)

# to traverse single elements:
for j in arr1:
    for k in j:
        print(k)


# in 3d array:
arr2=np.array([[[1,2,3],[4,5,6]]])
print(arr2)
for i in arr2:
    for j in i:
        for k in j:
            print(k)


# for iteration we use numpy function called (nditer):
arr3=np.array([[[1,2,3],[4,5,6]]])
print(arr3)
for i in np.nditer(arr3):
    print(i)


# for larger array or if we want indexes we use (ndenumerate)
arr4=np.array([[[1,2,3],[4,5,6]]])
print(arr4)
for i in np.ndenumerate(arr4):
    print(i)


# copy function:
arr5=np.array([1,2,3,4])
print("arr5: ",arr5)
co=arr5.copy()
print("copy: ",co)


# view function:
arr6=np.array([1,2,3,4])
print ("arr5: ",arr5)
vi=arr6.view()
print("view: ",vi)

# in copy function if we change original array copy array doesnot change
# in view function if we change in original aaray copy array will also b change