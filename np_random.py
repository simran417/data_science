import numpy as np
#to create array with random number:
## rand function() (values always lies b/w 0&1)
arr1=np.random.rand(6)
print("for single dimension", arr1)
#for multiple dimension:
arr2=np.random.rand(3,6)
print("for multiple dimension", arr2)

#randn function():  (it gives value close to zero)
arr3=np.random.randn(7)
print("randn function: ",arr3)

#ranf function():  (it gives values less than 1)
arr4=np.random.ranf(5)
print("ranf function: ",arr4)

#randint function(): np.random.randint(min,max,total_no.)
arr5=np.random.randint(0,10,5)
print("randint function: ", arr5)