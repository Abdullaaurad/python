import numpy as np

def create(x):
    return np.zeros((x, x))

def printG(x,matrix):
    print("   ",end="")
    for i in range(x):
        print(i,end="  ")
    print("\n")
    for i in range(x):
        print(i,end="  ")
        for k in range(x):
           print(int(matrix[i][k]),end="  ") 
        print("\n")

def AddEdge(source,destination,matrix):
    matrix[source][destination]=1

def RemoveEdge(source,destination,matrix):
    matrix[source][destination]=0

def SearchEdge(source,destination,matrix):
    if(matrix[source][destination]==0):
        print("Edge not in graph")
    else:
        print("Edge is represented in graph")

def AddVertices(matrix,x,y):
    new=np.zeros((x+y, x+y))
    for i in range(x):
        for k in range(x):
            new[i][k]=matrix[i][k]

    return new

def RemoveVertices(matrix,x,y):
    new=np.zeros((x-y, x-y))
    for i in range(x-y):
        for k in range(x-y):
            new[i][k]=matrix[i][k]

    return new

matrix=None
x = int(input("Enter how many vertices in graph: "))
matrix=create(x)
y = int(input("Enter how many edges in graph: "))
for i in range(y):
    print(f"\nEnter source and destination of Edge {i+1}")
    source=int(input("Enter source ="))
    destination=int(input("Enter destination ="))
    AddEdge(source,destination,matrix)

z = int(input("Enter how many vertices to remove: "))
for i in range(z):
    print(f"\nEnter source and destination of Edge {i+1}")
    source=int(input("Enter source ="))
    destination=int(input("Enter destination ="))
    RemoveEdge(source,destination,matrix)

print(f"\nEnter source and destination of Edge to search")
source=int(input("Enter source ="))
destination=int(input("Enter destination ="))
SearchEdge(source,destination,matrix)

a = int(input("Enter how many vertices to add: "))
matrix=AddVertices(matrix,x,a)
x=x+a

b = int(input("Enter how many vertices to add: "))
matrix=AddVertices(matrix,x,b)
x=x-b

printG(x,matrix)