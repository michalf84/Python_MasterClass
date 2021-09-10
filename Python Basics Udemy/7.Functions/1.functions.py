def multiply():
    result=10.5*4
    return result

answer=multiply()
print(answer)

print("*"*30)

def multiply2(x,y):
    result=x+y
    return result

answer=multiply2(1,3)
print(answer)
print("*"*30)

for val in range(1,5):
    two_times=multiply2(2,val)
    print(two_times)


def is_palindrome(string):
    backwards=string[::-1]
    return backwards==string #if equal reutrsn tru eand returs value

# another method
def is_palindrome2(string):
    return string[::-1].casefold()==string.casefold() #if equal reutrsn tru eand returs value
# ----------------
word='olo'
if is_palindrome2(word):
    print("is paligrome")
else:
    print("not paligrome")
# --------------------
def is_palindromesentence(string):
    sentence=""
    for char in string:
        if char.isalnum():
            sentence+=char
    return string[::-1].casefold()==string.casefold() #if equal reutrsn tru eand returs value

is_palindromesentence("ho ho")

# FUNCION CALLING FUNCION

def is_palindromesentence2(string:str)->bool:
    sentence=""
    for char in string:
        if char.isalnum():
            sentence+=char
    return is_palindrome2(sentence)

is_palindromesentence2("hoho")

def fibonaci(n):
    """Return n th Fibonacci number, for positive n."""
    if 0<=n<=1:
        return n
    n_minus1,n_minus2=1,0
    result=None
    for f in range (n-1):
        resuSlt=n_minus2+n_minus1
        n_minus2=n_minus1
        n_minus1=result
    return result

for i in range(36):
    print(i,fibonaci(i))