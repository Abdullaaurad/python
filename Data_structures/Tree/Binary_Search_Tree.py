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

def PostOrderTraversal(head):
    if head is None:
        return   
    PostOrderTraversal(head.left)
    PostOrderTraversal(head.right)
    print(head.data,end=" ")

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
        return (head.data)
    else:
        MaxValue(head.right)
    
def MinValue(head):
    if head is None:
        print("The tree is empty")
    elif(head.left==None):
        print(f"min value ={head.data}")
    else:
        MaxValue(head.left)

def Height(head):
    if head is None:
        return 0
    return 1+(max(Height(head.left),Height(head.right)))

def Size(head):
    if head is None:
        return 0
    return 1+Height(head.left)+Height(head.right)

def MirrorImage(head):
    if head is None:
        return
    MirrorImage(head.left)
    MirrorImage(head.right)
    temp=head.left
    head.left=head.right
    head.right=temp
    return head

def Search(head,value):
    if head is None:
        print("Error")
    elif(value>head.data):
        Search(head.right,value)
    elif(value<head.data):
        Search(head.left,value)
    else:
        print("The value is found")

def Delete(head,value):
    if head is None:
        print("value is not inside Tree")
        return head
    elif(value<head.data):
        head.left=Delete(head.left,value)
    elif(value>head.data):
        head.right=Delete(head.right,value)
    else:
        if head.left is None:
            temp = head.right
            head = None
            return temp
        elif head.right is None:
            temp = head.left
            head = None
            return temp
        
        temp = MaxValue(head.left)
        head.data = temp
        head.left = Delete(head.left,temp)
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

print("\nPost-order traversal:")
PostOrderTraversal(head)

'''
MaxValue(head)
MinValue(head)

print(f"\nThe Height of the Tree ",Height(head))
print(f"The size of the Tree ",Size(head))


print("\nMirror Image of tree:")
new =MirrorImage(head)
InOrderTraversal(new)

ID=int(input("\nEnter the value to search ="))
Search(head,ID)

ID=int(input("\nEnter the value to delete ="))
Delete(head,ID)

print("\nIn-order traversal:")
InOrderTraversal(head)
'''