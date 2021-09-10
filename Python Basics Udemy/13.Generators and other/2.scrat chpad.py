a=2
b=3
print("a is {} b is {}".format(a,b))

a,b=b,a
print("a is {} b is {}".format(a,b))

def fibinacci():
    current=0
    previous=1
    while True:
        yield current
        current,previous=current+previous,current


fib=fibinacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

def oddnumbers():
    n=1
    while True:
        yield n
        n+=2

odds=oddnumbers()


def pi_series():
    odds=oddnumbers()
    approximation=0
    while True:
        approximation+=(4/next(odds))
        yield approximation
        approximation-=(4/next(odds))
        yield approximation

print()
print()

approx_pi=pi_series()

for x in range(10):
    print(next(approx_pi))