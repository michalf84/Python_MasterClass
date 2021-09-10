
choice="-"
while choice!="0":
    if choice in "12345":
        print(f"you chose {choice}")
    else:
        print("pleaes choose option from the list")
        print("1:\t learn Python")
        print("2\tlearn Java")
        print("3:\tGo swimming")
        print("4\t go to bed")
        print("0\t exit")

    choice=input()
