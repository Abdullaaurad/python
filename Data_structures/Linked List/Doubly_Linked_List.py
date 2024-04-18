class Node:
    def __init__(self,Name,Marks):
        self.Name=Name
        self.Marks=Marks
        self.next=None
        self.previous=None
    
    def printNode(self):
        print(f"\nThe student Name ={self.Name}")
        print(f"The student Marks ={self.Marks}")

    def edit(self,value):
        if(type(value)==str):
            self.Name=value
        else:
            self.Marks=value

def createNode():
    Name=str(input("Enter student Name ="))
    Marks=int(input("Enter marks of student ="))
    return Node(Name,Marks)

def PrintList(head):
    current = head
    while current:
        current.printNode()
        current = current.next

def Add(head):
    new_node=createNode()
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    new_node.previous=current
    return head
    
def Remove(head, Name):
    if not head:
        print("List is empty.")
        return None
    if head.Name == Name:
        (head.next).previous=None
        return head.next
    prev = None
    current = head
    while current and current.Name != Name:
        prev = current
        current = current.next
    if not current:
        print("Student not found.")
        return head
    ptr=current.next
    prev.next = ptr
    ptr.previous=prev
    return head

def Search(head, Name):
    current = head
    while current:
        if current.Name == Name:
            current.printNode()
            return
        current = current.next
    print("Student not found.")

def Min(head):
    if not head:
        print("List is empty.")
        return
    current=head
    Min=current
    while(current):
        if(current.Marks<Min.Marks):
            Min=current
        current=current.next
    Min.printNode()

def Max(head):
    if not head:
        print("List is empty.")
        return
    current=head
    Max=current
    while(current):
        if(current.Marks>Max.Marks):
            Max=current
        current=current.next
    Max.printNode()

x = int(input("Enter how many elements to enter: "))
head=None
for i in range(x):
    print("\n\t\tEnter details of Student ",i+1)
    head=Add(head)

PrintList(head)

Name=str(input("\nEnter student Name to remove ="))
head=Remove(head,Name)
PrintList(head)

ID=input("\nEnter the student name to search =")
Search(head,ID)

print("Details of student having min marks",end="")
Min(head)
print("Details of student having max marks",end="")
Max(head)

