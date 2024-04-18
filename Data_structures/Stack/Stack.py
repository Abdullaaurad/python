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

def search(value):
    global Top
    found=0
    k=0
    while(k<=Top):
        if(Stack[k]==value):
            found=1
            print("Value is found on index =",k)
            break
        k=k+1
    if(found==0):
        print("The value is not in Stack")

x = int(input("Enter how many elements to enter: "))
for i in range(x):
        print("Enter element", i, "=", end="")
        y = int(input())
        Push(y)

print("Top element in Stack =",Pop())
peek()
search(5)
print("Stack:", Stack)