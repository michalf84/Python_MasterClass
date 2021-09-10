available_parts=["computer",
                 "monitor",
                 "keyboard",
                 "mouse",
                 "mouse mat",
                 "hdmi cable",
                 "dvd drive"]
valid_choices=[str(i) for i in range(1,len(available_parts)+1)]
print(valid_choices)
current_choice="-"
computer_parts=[]
1
while current_choice!="0":
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        index=int(current_choice)-1
        chosen_part=available_parts[index]
        if chosen_part in computer_parts:
            #it is already in so remove it
            # pass
            computer_parts.remove(chosen_part)
        else:
            computer_parts.append(chosen_part)
        print(f"Your list now contains{computer_parts}")
    else:
        print("Please add options from the list below")
        for number,part in enumerate(available_parts):
            print(f"{number+1}: {part}")
    current_choice=input("choose option")
print(computer_parts)

