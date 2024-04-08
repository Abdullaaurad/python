class MyClass1:
    def my_method(self, arg1, arg2=None):
        if arg2 is None:
            print("One argument provided:", arg1)
        else:
            print("Two arguments provided:", arg1, arg2)

obj = MyClass1()
obj.my_method(1)
obj.my_method(1, 2)

class MyClass2:
    def my_method(self, **kwargs):
        if 'arg1' in kwargs and 'arg2' in kwargs:
            print("Two arguments provided:", kwargs['arg1'], kwargs['arg2'])
        elif 'arg1' in kwargs:
            print("One argument provided:", kwargs['arg1'])

obj = MyClass2()
obj.my_method(arg1=3)
obj.my_method(arg1=3, arg2=4)

class MyClass3:
    def my_method(self, *args):
        if len(args) == 1:
            print("One argument provided:", args[0])
        elif len(args) == 2:
            print("Two arguments provided:", args[0], args[1])

obj = MyClass3()
obj.my_method(5)
obj.my_method(5,6)

