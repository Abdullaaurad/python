Max_Size=100
Queue=[None] * Max_Size
Front=-1
Rear=-1

def IsEmpty():
    if(Front==-1):
        return True
    else:
        return False
    
def IsFull():
    if(Rear==Max_Size-1):
        return True
    else:
        return False

def Enqueue(value):
    global Front,Rear
    if(IsFull()):
        return "The queue is full"
    else:
        if(IsEmpty()):
            Front=Front+1
        Rear=Rear+1
        Queue[Rear]=value

def Dequeue():
    global Front,Rear
    if(IsEmpty()):
        return "The Queue is Empty"
    else:
        value=Queue[Rear]
        if(Front+1==Rear):
            Front=-1
            Rear=-1
            return value
        else:
            Front+=1
            return value

def search(value):
    global Front, Rear
    found = False
    for i in range(Front, Rear + 1):
        if Queue[i] == value:
            found = True
            print("Value is found at index =", i)
            break
    if not found:
        print("The value is not in Queue")

def printStack():
    for i in range(Front,Rear+1):
        print(Queue[i],end=" ")

x = int(input("Enter how many elements to enter: "))
for i in range(x):
        print("Enter element", i, "=", end="")
        y = int(input())
        Enqueue(y)

print("Top element in Queue =",Dequeue())
search(5)
printStack()