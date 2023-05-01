"""Dog Module
    This module does activity of the DOG
"""
#docstrings : just similar to comment to remember the main points in future 
class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Intialize a new Dog"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""    
        print('Bo Bo')


print(help(Dog))