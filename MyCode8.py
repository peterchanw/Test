# lambda function (function without a name for simple tasks
from functools import reduce

def add(a,b):
    return a+b

result1 = add(5,6)
print(result1)

f = lambda a,b : a+b
result2 = f(5,6)
print(result2)

nums = [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n:n%2==0,nums))
doubles = list(map(lambda n:n*2,evens))
sum = reduce(lambda a,b:a+b,doubles)
print(evens)
print(doubles)
print(sum)