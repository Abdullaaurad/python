class MyClass:
    def public_method(self):
        print("This is a public method.")

    def public_attribute(self):
        self.public_var = 10

    def _private_method(self):                #Can still access it
        print("This is a private method.")    #we use(_) this to tell the programmers that it is a private function 
                                              #there are no excess specifiers in python
new = MyClass()
new.public_method()
new.public_attribute()
new._private_method()