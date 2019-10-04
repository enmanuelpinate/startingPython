#STR AND REPR

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "String representation of this object"

    def __repr__(self):
        return "__repr__ method"

bob = Person("Bob", 35)
print(bob)