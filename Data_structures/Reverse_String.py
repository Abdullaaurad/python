Stack=[]
Top=-1

def IsEmpty():
    if(Top==-1):
        return True
    else:
        return False
    
def peek():
    global Top
    value=Stack[Top]
    print("Top element =",value)

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

def printStack():
    for i in range(Top+1):
        print(Stack[i],end="")

string=str(input("Enter string to reverse ="))
for char in string:
    Push(char)

printStack()