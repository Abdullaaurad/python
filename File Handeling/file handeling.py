print("Hi")
#x=10
#if x==10:
#    print("true")
#else:
#    print("false")

#for i in range (10):
#    print(i+1)

#y=int(input("Enter a number for y :"))
#print(y)

#def greet(name):
#    print("Hello", name)

#greet("abdulla")

#y=7.8
#z=int(y)
#print(z)
#string=input("Enter a string :")
#print(string)

#f = open("hi.txt","w")
#string="hello"
#f.write(string)
#f.close()


f = open("hi.txt", "a")
string="hello world"
f.write(string)
f.close()

f = open("hi.txt", "r")
for word in f:
    print(word,end=(""))
f.close()  
#content=f.read()
#print(f.readline(),end="")
#print(f.readline(),end="")
#print(f.readline())
#f.close()

#content=f.split(" ")
#print(content)

Array=[1,2,3,4]
for i in range (3):
    print("\n",Array[i])

print("Hi")
