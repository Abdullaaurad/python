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
    value=Stack[0]
    Stack.pop(0)
    Top=Top-1
    return value

Correct=1
string=str(input("Enter string to check ="))
for char in string:
    if(char=='(' or char=='{' or char=='['):
        Push(char)
    elif(char==')' or char=='}' or char==']'):
        if(IsEmpty()):
            Correct=0
            break
        else:
            c=Pop()
            if(char==')' and c!='('):
                Correct=0
                break
            elif(char=='}' and c!='{'):
                Correct=0
                break
            elif(char==']' and c!='['):
                Correct=0
                break

if(not IsEmpty()):
    Correct=0

if(Correct==0):
    print("The statement is wrong")
else:
    print("The statement is correct")