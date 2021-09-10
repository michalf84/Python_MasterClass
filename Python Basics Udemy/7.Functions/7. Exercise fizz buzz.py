def fizz_buzz(number: int) -> str:
    """
    Play Fizz buzz

    :param number: The number to check.
    :return: 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if number % 15 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# for i in range(1, 101):
#     print(fizz_buzz(i))

#  NEew game

input("Play fizz buzz. Pres enter to start")
print()

next_number=0
while next_number<99:
    next_number+=1
    print(fizz_buzz(next_number))
    next_number+=1
    correct_answer=fizz_buzz(next_number)
    players_answer=input("Your go: ")
    if players_answer!=correct_answer:
        print(f"you loose, the correct anwer was {correct_answer}")
        break
else:
    print(f"well done you reached {next_number}")