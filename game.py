import random
 
def game(comp,you):
    if comp==you:
        return None
    if comp=='s':

        if you=='w':
            return False
        elif you=='g':
            return True
        
    if comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True  

    if comp=='g':
        if you=='s': 
            return False
        elif you=='w':
            return True        

random_no = random.randint(1,3)
if random_no ==1:
    comp='s'

elif random_no ==2:
    comp = 'w'

elif random_no==3:
    comp ='g'

you=input("your turn: snake(s), water(w), gun(g)")    
a=game(comp,you)
print(f"you choose: {you}")
print(f"comp choose: {comp}")
 
if a == None:
    print("tie") 
elif a== True:
    print("you win")
else:
    print("you lose")    
      



