class Vertex:
    def __init__(self,value):
        self.value=value
        self.edge=None
        self.next=None

class Edge:
    def __init__(self,value):
        self.value=value
        self.next=None

def create(x):
    head=None
    ptr=None
    for i in range(x):
        if(i==0):
            N = Vertex(0)
            head=N
            ptr=N
        else:
            N = Vertex(i)
            ptr.next=N
            ptr=ptr.next

    return head

def AddEdge(source, destination, head):
    ptr = head
    while ptr.value != source and ptr is not None:
        ptr = ptr.next

    if ptr is None:
        return "Source is not found in Graph"
    else:
        if ptr.edge is None:
            ptr.edge = Edge(destination)
        else:
            k = ptr.edge
            while k.next is not None:
                k = k.next
            k.next = Edge(destination)
    return head

def printG(head):
    ptr=head
    while(ptr is not None):
        if(ptr.edge is not None):
            print(ptr.value,"-> ",end="")
            e=ptr.edge
            while(e is not None):
                if(e.next is None):
                    print(e.value)
                else:
                    print(e.value,"-> ",end="")
                e=e.next
        else:
            print(ptr.value)
        ptr=ptr.next


def RemoveEdge(source,destination,head):
    ptr=head
    while(ptr.value != source and ptr is not None):
        ptr=ptr.next
    if(ptr is None):
        print("Source is not found in Graph")
        return head
    else:
        Node=ptr.edge
        pre=None
        while(Node.value != destination and Node is not None):
            pre=Node
            Node=Node.next
        if(Node is None):
            print("destination is not found in Graph")
            return head
        else:
            if pre is not None:
                pre.next = Node.next
            else:
                ptr.edge = Node.next
    return head       

def SearchEdge(source,destination,head):
    ptr=head
    while(ptr.value != source and ptr is not None):
        ptr=ptr.next
    if(ptr is None):
        print ("Source is not found in Graph")
    else:
        Node=ptr.edge
        while(Node.value != destination and Node is not None):
            Node=Node.next
        if(Node is None):
            print ("destination is not found in Graph")
        else:
            print ("Edge is found in graph")


def AddVertices(head):
    n=0
    ptr=head
    while(ptr.next is not None):
        ptr=ptr.next
        n=n+1
    ptr.next=Vertex(n+1)
    return head

def RemoveVertices(head,value):
    ptr=head
    pre=None
    while(ptr.value != value):
        pre=ptr
        ptr=ptr.next
    if(ptr is not None):
        if pre is not None:
            pre.next = ptr.next
        else:
            head = ptr.next

    ptr = head
    while ptr is not None:
        Edge = ptr.edge
        pre = None
        while Edge is not None:
            if Edge.value == value:
                if pre is not None:
                    pre.next = Edge.next
                else:
                    ptr.edge = Edge.next
                break
            pre = Edge
            Edge = Edge.next
        ptr = ptr.next

    return head


matrix=None
x = int(input("Enter how many vertices in graph: "))
matrix=create(x)

y = int(input("Enter how many edges in graph: "))
for i in range(y):
    print(f"\nEnter source and destination of Edge {i+1}")
    source=int(input("Enter source ="))
    destination=int(input("Enter destination ="))
    matrix=AddEdge(source,destination,matrix)

'''
z = int(input("Enter how many edges to remove: "))
for i in range(z):
    print(f"\nEnter source and destination of Edge")
    source=int(input("Enter source ="))
    destination=int(input("Enter destination ="))
    Matrix=RemoveEdge(source,destination,matrix)
    
print(f"\nEnter source and destination of Edge to search")
source=int(input("Enter source ="))
destination=int(input("Enter destination ="))
SearchEdge(source,destination,matrix)
'''

matrix=AddVertices(matrix)
printG(matrix)

b = int(input("Enter value of vertex to remove: "))
matrix=RemoveVertices(matrix,b)

printG(matrix)