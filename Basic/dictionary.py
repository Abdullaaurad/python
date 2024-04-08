dictionary={'a':12,'b':34,'c':56,'a':100}
print(dictionary)

#In a dictionary we need to give unique names for its keys if not the value will be replaced from left to right like variables
#print(dictionary[1]) (will give us a error we cant access them like in arrays)

print(dictionary['a']) #we have to specify its key name to access the values inside them
dictionary['c']=1
print(dictionary)

dictionary['e']="abdulla" #can have multiple data types
dictionary['d']=dictionary['a']  #we can add keys to dictionary like this too
print(dictionary)
print(sorted(dictionary))
for item in dictionary:
    print(item,":",dictionary[item])
print("The length of dictionary",len(dictionary))

if 'a' in dictionary:
    print("a in dictionary")
else:
    print("a not in dictionary")

for key,value in dictionary.items():
    print(key,":",value,"\t")

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())