'''#to read files:
f = open("sample.txt", "r")
data = f.read() #read complete file read(5) reads only 5 character
print(data)
f.close()'''

'''#readline function:(read only one line)
f = open("sample.txt", "r")
data = f.readline()
print(data)
f.close()'''

'''#write in files:
f = open("another.txt", "w")
data = f.write("this is another file")
f.close()'''


'''#append function:
f = open("another.txt", "a")
data = f.write("i m append")
f.close()'''

#with function:
with open("another.txt") as f:
    f.read()