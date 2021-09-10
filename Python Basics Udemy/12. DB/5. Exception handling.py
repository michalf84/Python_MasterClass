def factorial(n):
    
    if n<=1:
        return 1
    else:
        print(n/0)
        return n*factorial(n-1)


try:
    print(factorial(1000))
except RecursionError:
    print("this program calculate faactorioals that large")
except ZeroDivisionError:
    print("don't divide by zero")

# except (RecursionError,ZeroDivisionError):
#     print("Error")

print("program terminating")