Stack=[]
Top=-1

def IsEmpty():
    if(Top==-1):
        return True
    else:
        return False
    
def Push(value):
    global Top
    Stack.insert(0,value)
    Top=Top+1

def Pop():
    global Top
    if(IsEmpty()):
        return "Stack is Empty"
    value=Stack[0]
    Stack.pop(0)
    Top=Top-1
    return value

x = int(input("Enter how many elements to enter: "))
for i in range(x):
        print("Enter element", i, "=", end="")
        y = int(input())
        Push(y)

print("Top element in Stack =",Pop())

print("Stack:", Stack)