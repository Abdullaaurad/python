#there aren't any specific data type as struct we use 
class Point:
    def __init__(self, data):
        self.x = data
        self.next = None


point1 = Point(10)
point2 = Point(20)

print(point1.x)
print(point1.next)
point1.next=point2
print(point1.next.x)
