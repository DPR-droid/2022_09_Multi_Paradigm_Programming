# Page 11 of lecture

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'Person("{self.name}",{self.age})'

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
print(p1)