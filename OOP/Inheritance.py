class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "makes Noise"

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} dog of {self.age} says woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"


dog1 = Dog("Buddy",6)
#dog2 = Dog("Puppy")   To do this we have to use constructor overloading
cat = Cat("Whiskers")
A1 = Animal("Bird")

print(dog1.speak()) 
print(cat.speak())
print(A1.speak())
