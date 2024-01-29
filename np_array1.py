'''#creating array:
import numpy as np
x=[1,2,3,4]
y=np.array(x)
print(y)'''

'''#another method:
import numpy as np
x=[1,2,3,4,5]
y=np.array([1,2,3,4,5]) #we can directly put values 
print(y)  
print(type(y))  #to check the type'''

'''#to take input from user:
import numpy as np

l =[] #empty list
for i in range(1,5): #loop for 4 no. 
    user_input =int(input("enter no. "))#if we not write string it will give string value but we need integer value 
    l.append(user_input)#append function add value in last position

print(np.array(l))   '''

'''#to check the dimension of array we use ndim function
import numpy as np
y=np.array([1,2,3,4])
print(y)
print(y.ndim)'''

'''#for 2 d array (when we pass two lists no. of items should be same)
import numpy as np
y=np.array([[1,2,3,4],[5,6,7,8]])
print(y)
print(y.ndim)'''

'''#for 3-d arrays:
import numpy as np
y=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]]])
print(y)
print(y.ndim)'''

#for n-d array (ndmin function is used to create dimension of array)
import numpy as np
y=np.array([1,2,3,4],ndmin=10)
print(y)
print(y.ndim) 