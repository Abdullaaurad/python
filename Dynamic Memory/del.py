import gc

class MyClass:
    def __init__(self, data):
        self.data = data

    def printf(self):
        print("date is =",self.data)

obj1 = MyClass(10)
obj2 = obj1
obj2.printf()

# Deleting obj1 (but obj2 still refers to the object)
del obj1
print("After deleting Obj1")
obj2.printf()
#!obj1.printf()    doesn't exist

# Manually triggering garbage collection
gc.collect()
