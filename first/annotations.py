# annotations

def increnent(n: int) -> int:
    return n + 1


# same with the variable

cont: int = 0


#exceptions
# try 

class DogNotFoundException(Exception):
    print("in the exception class")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Sorry this bread not available")

try:
    result = 2 / 0
except ZeroDivisionError:
    print('cannot divide by the Zero!')
finally:
    result = 1

print(result)
