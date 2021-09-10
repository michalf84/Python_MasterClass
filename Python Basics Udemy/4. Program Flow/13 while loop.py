# for i in range(10):
#     print(f"i is now{i}")

i=0

while i<10:
    print(f"i is now {i}")
    i+=1

# new code

available_exit=["north","south","east","west"]
chosen_exist=""

while chosen_exist not in available_exit:
    chosen_exist=input("choose exist: ")
    if chosen_exist.casefold()=="quit":
        print("game over")
        break
else:
    print("arent you glad it is over")