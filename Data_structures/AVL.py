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

def PreOrderTraversal(head):
    if head is None:
        return   
    print(head.data,end=" ")
    PreOrderTraversal(head.left)
    PreOrderTraversal(head.right)

def AddNode(head,value):
    if head is None:
        return Node(value)
    elif(value<(head.data)):
        head.left=AddNode(head.left,value)
    elif(value>(head.data)):
        head.right=AddNode(head.right,value)
    return Balance(head)

def MaxValue(head):
    if head is None:
        return None
    elif(head.right==None):
        print(f"\nmax value ={head.data}")
    else:
        MaxValue(head.right)

def Height(head):
    if head is None:
        return 0
    return 1+(max(Height(head.left),Height(head.right)))

def BalanceFactor(head):
    if head is None:
        return 0
    return (Height(head.left)-Height(head.right))

def RightRotate(head):
    x=head.left
    y=x.right

    x.right=head
    head.left=y
    return x

def LeftRotate(head):
    x=head.right
    y=x.left

    x.left=head
    head.right=y
    return x

def Balance(head):
    if(BalanceFactor(head)>1 and BalanceFactor(head.left)>=0):
        return RightRotate(head)
    if(BalanceFactor(head)>1 and BalanceFactor(head.left)<0):
        head.left=LeftRotate(head.left)
        return RightRotate(head)
    if(BalanceFactor(head)< -1 and BalanceFactor(head.right)>=0):
        return LeftRotate(head)
    if(BalanceFactor(head)< -1 and BalanceFactor(head.right)<0):
        head.right=RightRotate(head.right)
        return LeftRotate(head)
    return head

x = int(input("Enter how many elements to enter: "))
head=None
for i in range(x):
    print(f"\nEnter the value of Node {i+1}=",end="")
    value=int(input())
    head=AddNode(head,value)

print("\nIn-order traversal:")
InOrderTraversal(head)

print("\nPre-order traversal:")
PreOrderTraversal(head)