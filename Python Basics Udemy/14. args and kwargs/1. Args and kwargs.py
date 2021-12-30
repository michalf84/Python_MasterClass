# /*
# *args in function definitions in python is used to pass n number of arguments to a function i.e.
# there is no need to define the number of arguments at the time of creating the function.
# Syntax: Use the symbol * to take in n number of arguments. It is often used with the word 'args',
# however we can use any other word.
# For example : we want to make a multiply function that takes any number of arguments and able
# to multiply them all together. It can be done using *args.*/

# * indicates that number of arguments can be taken
def Multiple(*args):
    for parameter in args:
        print (parameter)
    #call the function
print(Multiple("Lets","learn","Python","for","Data","Science") )

# **kwargs
# A keyword argument is where you provide a name to the variable as you pass it into the function.
# For example, func('Sex'=Female) The special syntax **kwargs in function definitions in python is used
# to pass a keyworded, variable-length argument list. We use the name kwargs with the double star.
# The reason is because the double star allows us to pass through keyword arguments (and any number of them).
# We can use any other name instead of kwargs.
# One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it.

def function(**kwargs):
    for a,b in kwargs.items():
        print(a,"==",b)
# call the function
print( a=function(A = "First letter", B = "Second letter", C = "Thirs letter"))