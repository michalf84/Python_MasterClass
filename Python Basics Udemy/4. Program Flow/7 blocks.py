name=input("enter your _name: ")
age=int(input(f"how old are you,{name}"))

if age>=18:
    print("you can vote")
    print("please put an x in the box")
else:
    print("you cannot vote")

if age<18:
    print("you can NOT vote")
    print("please put an x in the box")
elif age==18:
    print("third scenario")
else:
    print("you CAN vote")


