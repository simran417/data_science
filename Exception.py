'''a = input("enter no. ")
print(f"the table of{a} is: ")
try: 
  for i in range(1,11):
    print(f"{int(a)}X{int(i)} = {int(a)*i}")
except Exception as e:
  print("some error")

print("some line of code")
print("end")

#some specific errors:
try:
  b = int(input("enter no.: "))
  num = [3,4,5]
  print(num[b])

except ValueError:
  print("invalid no.")
except IndexError: 
  print("invalid index")'''

'''#use of finally:
def fun():
 try:
  a = int(input("enter no.: "))
  l = [3,4,5]
  print(l(a))
  return 1
 except:
  print("invalid index")
  return 0
 finally:
   print("i m executed") 

b = fun()
print(b)'''

#custom exception:

a = int(input("enter no.: "))
if(a>5 or a<9):
  raise ValueError("invalid value")

