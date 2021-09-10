# What is List Comprehension?
# It is an elegant way of defining and creating a list. List Comprehension allows us to create a list using for loop with lesser code. What normally takes 3-4 lines of code, can be compressed into just a single line.
#
# Example:
#
# # initializing the list
# list = []
#
# for i in range(11):
#     if i % 2 == 0:
#         list.append(i)
#
# # print elements
# print(list)
# Output:
#
# 0 2 4 6 8 10
# Now, the same output can be derived from just a single line of code.
#
# list = [i for i in range(11) if i % 2 == 0]
# print(list)
# Output:
# What are Generator Expressions?
# Generator Expressions are somewhat similar to list comprehensions, but the former doesn’t construct list object.
# Instead of creating a list and keeping the whole sequence in the memory, the generator generates the next element in demand.
# When a normal function with a return statement is called, it terminates whenever it gets a return statement.
# But a function with a yield statement saves the state of the function and can be picked up from the same state, next time the function is called.
# The Generator Expression allows us to create a generator without the yield keyword.
#
# Syntax Difference: Parenthesis are used in place of square brackets.
#
# # List Comprehension
# list_comprehension = [i for i in range(11) if i % 2 == 0]
#
# print(list_comprehension)
# Output:
#
# 0 2 4 6 8 10
# # Generator Expression
# generator_expression = (i for i in range(11) if i % 2 == 0)
#
# print(generator_expression)
# Output:
#
# <generator object  at 0x000001452B1EEC50>
# So what’s the difference between Generator Expressions and List Comprehensions?
# The generator yields one item at a time and generates item only when in demand. Whereas, in a list comprehension, Python reserves memory for the whole list. Thus we can say that the generator expressions are memory efficient than the lists.
# We can see this in the example below.

burgers=["beef","chicken","spicy bean"]
toppings=["cheese","egg","beans","spam"]

meals=[(burger,topping)for burger in burgers for topping in toppings]
print(meals)

print("-"*100)
for burger in burgers:
    for topping in toppings:
        print((burger,topping))
#nested list with tuples
meals=[[(burger,topping)for burger in burgers] for topping in toppings]
print(meals)

print()

for i in range(1,11):
    for j in range (1,11):
        print(i,i*j)

for x,y in [(i,i*j) for i in range(1,11) for j in range (1,11)]:
    print(x,y)
times2= [(i,i*j) for i in range(1,11) for j in range (1,11)]
print(times2)
