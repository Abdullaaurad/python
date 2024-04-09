class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def InOrderTraversal(head):
    if head is None:
        return   
    InOrderTraversal(head.left)
    print(head.data,end=" ")
    InOrderTraversal(head.right)

def AddNode(head,value):
    if head is None:
        return Node(value)
    elif(value<(head.data)):
        head.left=AddNode(head.left,value)
    elif(value>(head.data)):
        head.right=AddNode(head.right,value)
    return head

def MaxValue(head):
    if head is None:
        print("The tree is empty")
    elif(head.right==None):
        print(f"\nmax value ={head.data}")
    else:
        MaxValue(head.right)

def Height(head):
    if head is None:
        return 0
    return 1+(max(Height(head.left),Height(head.right)))

x = int(input("Enter how many elements to enter: "))
head=None
for i in range(x):
    print(f"\nEnter the value of Node {i+1}=",end="")
    value=int(input())
    head=AddNode(head,value)

print("\nIn-order traversal:")
InOrderTraversal(head)

