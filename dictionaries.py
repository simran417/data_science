#dictionaries:
dic={
    "marks":[1, 2, 3],
    "name": "simran",
    "greeting": "good morning",
    "dic2":{'cast':'vohra' }
}
'''print(dic['name'])
#to change marks:
dic['marks']=[3,6,9]
print(dic['marks'])
print(dic['dic2'])'''

#dictionaries methods:
print(dic.keys())
print(dic.values())
print(dic.items())
upddic={
    "sneha":"friend"
}
dic.update(upddic)
print(dic)
print(dic.get("name"))#if the value is not present in it it give none ; print(dic['name']) returns an error