fruit={"orange":"a sweet fruit",
       "apple":"red fruit",
       "lemon":"yellow citrus fruint",
       "grape":"a msall sweet fruitn growning in branches"}

dict_key="apple" #input("enter fruin _name")

choice=fruit.get(dict_key,f"we donlt' ahve a {dict_key}")
print(choice)


print()
for snack in fruit:
    print(fruit[snack])

ordered_key=list(fruit.keys())
ordered_key.sort()

print("*"*20)
for i in ordered_key:
    print(fruit[i])

    # alternatives
print()
print("---Alternative 1")
for i in fruit.keys():
    print(fruit[i])

# alternative but less efficient
print()
print("---Alternative 2")
for i in fruit.values():
    print(i)

print()
print("fruit items")
print(fruit.items())
print()
f_tuple=tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item,description=snack
    print(item+ " is" + description)