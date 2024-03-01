#dictionary
"""
print("hi")
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
print(len(dictionary))

if 'a' in dictionary:
    print("a in dictionary")
else:
    print("a not in dictionary")

for key,value in dictionary.items():
    print(key,":",value,"\t")

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items()) """

#Array"
"""
Array=[2,6,8,9]
print(Array[0:3])
print(Array[1])  
Array[0]=5
Array.append(7)
Array.insert(1,21)
print(Array)
Array.pop()
Array.remove(6)
print(Array) """

"""
#sets
set={1,2,3,8,3,9,5,2,1,6,-3}
print(set)
print(len(set))
set.add('new')
set.remove('new')
print(set)
print(sum(set))
print(max(set))
print(min(set))
print(sorted(set))

for item in set:
    print(item,end="")  
"""

#tuples   tuples are read only cant change values or add values to it or delete  
"""
x=(3.9 , 3.5, 5, 7.9, 5, 2.3, 7.8)
print(x)
print(x[3])
print(x[1])
y=x[1:4]
print(y)
"""

print("Enter inputs :",end="")
x= input()
print("Enter inputs :",end="")
y= input()
print(x)