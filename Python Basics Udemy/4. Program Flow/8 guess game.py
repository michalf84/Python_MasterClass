answer=5
guess=int(input("enter your guesss: "))

if guess==answer:
    print("correct after first attempt")
else:
    if guess>answer:
        print("give smaller number")
    else:
        print("give higher number")
    guess=int(input())
    if guess==answer:
        print("you guessed")
    else:
        print("you did not guess")
