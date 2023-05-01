#recursion

def factorial(n):
    if n == 1: return 1
    return n * factorial(n  - 1)


print(factorial(5))

# decorators

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello()    