low=1
high=1000
guesses=1
print(f"provide a number between {low} and {high}")
input("please ENTER to start:")

guess=1
while low!=high:
    guess=low+(high-low)//2
    high_low=input(f"my guess is {guess} if higher press h is lower l or c if correct")

    if high_low=="h":
        low=guess+1
    elif high_low=="l":
        high=guess-1
    elif high_low=="c":
        print(f"I got it in {guesses} guesses")
        break
    else:
        print("enter h,l or c")
    guesses+=1
else: #note else is after while loop it is used as break code execution!!
    print(f"you thoutgh of the number{low}")
    print(f"I got it in {guesses} guesses")