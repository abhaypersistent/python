# lamda functions

lambda num : num  * 2

mutiply = lambda a,b : a * b

print(mutiply(7,6))

# map, reduce, filter

numbers = [1,2,3]

double = lambda a : a * 2

def doble(a):
    return a * 2

result = map(double, numbers)

print(list(result))