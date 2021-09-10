import timeit
import functools

def calc_values(x,y:int):
    return x+y

numbers=[2,3]

reduced_value=functools.reduce(calc_values,numbers)
print(reduced_value)

print(sum(numbers))