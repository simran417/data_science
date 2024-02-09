'''print("sum of previous no. and current no.")
previous_no=0
for i in range(1,11):
   sum = previous_no + i
   print(sum)
   previous_no = i'''
# 1st program:
# write a python program to calculate simple interest:
'''p=int(input("enter principal: "))
t=int(input("enter time period: "))
r=int(input("enter rate of interest: "))


def simple_interest(p,t,r):
    print("the principal is: ",p)   
    print("time period: ",t)
    print("rate of interest: ",r)
    si=(p*r*t)/100
    print("the simple interest is: ",si)
    return si

simple_interest(p,t,r)


# 2nd program:
num=int(input("enter the no."))

if(num>1):
    for i in range(2,(int(num/2))+1):
        if(num%i==0):
            print(num," is not a prime")
            break
        else:
            print(num," is prime")  
            break '''


# to count occurence of word in file:

count=0
f = open("C:/Users/hp/OneDrive/Desktop/Python/.idea/sample.txt","r")
data = f.read()
letter = input("enter word to be searched: ")
for i in range(0,len(data)):
    if(letter==data[i]):
        count=count+1
    
        
print(count)
f.close()