class header:
    def __init__(self, Data=0):
        self.Data = Data
        self.next = None

class Node:
    def __init__(self, Name=None, Marks=None):
        self.Name = Name
        self.Marks = Marks
        self.next = None
    
    def printNode(self):
        print(f"\nThe student Name = {self.Name}")
        print(f"The student Marks = {self.Marks}")

    def edit(self, value):
        if isinstance(value, str):
            self.Name = value
        else:
            self.Marks = value

def createNode():
    Name = input("Enter student Name = ")
    Marks = int(input("Enter marks of student = "))
    return Node(Name, Marks)

def PrintList(head):
    print("Number of nodes in list =",head.data)
    current = head.next
    while current:
        current.printNode()
        current = current.next

def Add(head):
    new_node = createNode()
    new_node.next = head.next  # Insert at the beginning of the list
    head.next = new_node
    head.Data+=1
    return head

def Remove(head, Name):
    prev = head
    current = head.next
    while current:
        if current.Name == Name:
            prev.next = current.next
            return head
        prev = current
        current = current.next
    print("Student not found.")
    return head

def Search(head, Name):
    current = head.next
    while current:
        if current.Name == Name:
            current.printNode()
            return
        current = current.next
    print("Student not found.")

def Min(head):
    current = head.next
    Min = current
    while current:
        if current.Marks < Min.Marks:
            Min = current
        current = current.next
    Min.printNode()

def Max(head):
    current = head.next
    Max = current
    while current:
        if current.Marks > Max.Marks:
            Max = current
        current = current.next
    Max.printNode()

x = int(input("Enter how many elements to enter: "))
head = header()  # Create header node
for i in range(x):
    print("\n\t\tEnter details of Student ", i + 1)
    head = Add(head)

PrintList(head)

ID = input("\nEnter the student name to search = ")
Search(head, ID)

Name = input("\nEnter student Name to remove = ")
head = Remove(head, Name)
PrintList(head)

Min(head)
Max(head)
