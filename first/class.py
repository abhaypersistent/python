# classes

# class Dog:
#     def bark(self):
#         print("bho bho")


# roger = Dog()

# print(type(roger))
# print(roger.bark())

# constructor

class Animal:
    def walk(self):
        print("Walking . . ...")

class Dog(Animal):
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("dsdsd")

roger = Dog("Moti", 12)

print(roger.name)
print(roger.age)
roger.bark()
roger.walk()