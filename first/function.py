def hello():
    print("hello")

hello()

# althoug it similar to the all regular functions
# dictionay is muttable

# scope of the variable
# nested functions

def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count()        


# closure

def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count
    
    return increment

    
increment = counter()

print(increment())
print(increment())
print(increment())


# talk("chant hare krishna and be happy")            