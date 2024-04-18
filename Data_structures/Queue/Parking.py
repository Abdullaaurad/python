Max_Size=100
Front=-1
Rear=-1

class Car:
    def __init__(self,ID,ArrivalTime):
        self.ID=ID
        self.ArrivalTime=ArrivalTime

    def printCar(self):
        print(f"The id of the Car ={self.ID}")
        print(f"The Arrival time of Car ={self.ArrivalTime}\n")

Queue=[None] * Max_Size

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
        else:
            Front+=1
        return value

def search(ID):
    global Front, Rear
    found = False
    for i in range(Front, Rear + 1):
        if Queue[i].ID == ID:
            found = True
            print("The car Arrived at =", Queue[i].ArrivalTime)
            break
    if not found:
        print("The car is not in the queue")

def printQueue():
    for i in range(Front,Rear+1):
        Queue[i].printCar()

def CreateObject(ID,ArrivalTime):
    C1 = Car(ID,ArrivalTime)
    return C1

x = int(input("Enter how many elements to enter: "))
for i in range(x):
        print("\n\t\tEnter details of Car ",i)
        print("Enter Car ID =", end="")
        ID =input()
        print("Enter Arrival time =", end="")
        ArrivalTime =input()
        C1=CreateObject(ID,ArrivalTime)
        Enqueue(C1)

print("Top First car in the Queue\n")
car=Dequeue()
car.printCar()

ID=input("Enter the ID of the car to search =")
search(ID)
printQueue()