import random

def get_integer(prompt):
    while True:
        temp=input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("It is invalid number error")

highest=10
guess=-10
answer=random.randint(1,highest)
print(str(answer) +"for testing")

guess=get_integer(": ")
while guess!=0:

    if guess==answer:
        print("correct answer")
        break
    else:
        if guess>answer:
            print("give smaller number")
            guess=get_integer(": ")
        else:
            print("give higher number")
            guess=get_integer(": ")

