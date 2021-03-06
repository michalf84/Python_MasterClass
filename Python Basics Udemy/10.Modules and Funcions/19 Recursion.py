def fact(n):
    # calculate n! iteratively
    result=1
    if n>1:
        for f in range(2,n+1):
            result*=f
    return result

def factorial(n):
#     n! can also be defined as n*(n-1)!
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)


def fib(n):
#     f(n)=F(n-1)+F(n-2)
    if n<2:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(130):
    print(i,fact(i))

for i in range(130):
    print(i,factorial(i))