# lamda functions
from functools import reduce

lambda num : num  * 2

mutiply = lambda a,b : a * b

# print(mutiply(7,6))

# map, reduce, filter

numbers = [1,2,3]

double = lambda a : a * 2

def doble(a):
    return a * 2

result = map(double, numbers)

# print(list(result))

numbers = [1,2,3]

def isEven(n):
    return n%2 == 0

# result = filter(isEven, numbers)

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))

# reduce 

expences = [
    ('Dinner', 80),
    ('car repair', 120)
]

sum = reduce(lambda a, b : a[1] + b[1], expences)

print(sum)

