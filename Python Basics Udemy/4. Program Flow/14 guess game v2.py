import random
highest=10
guess=-10
answer=random.randint(1,highest)
print(str(answer) +"for testing")




while guess!=answer:
    guess=int(input("enter your guess: "))
    if guess==answer:
        print("correct answer")
        break
    elif guess==0:
        break
    else:
        if guess>answer:
            print("give smaller number")
            guess=int(input("enter your guess: "))
        else:
            print("give higher number")
            guess=int(input("enter your guess: "))

