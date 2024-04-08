class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello,", self.name)


person1 = Person("Alice", 25)
person1 = Person("Alice")
print(person1.name)
person1.greet()
