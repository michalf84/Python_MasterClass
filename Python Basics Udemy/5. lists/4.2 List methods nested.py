even=[2,4,6,8]
odd=[1,3,5,7,9]
c=list(even+odd)
print(c)

numbers=[even,odd]
print(numbers)

print("For  valie in numbers:")
for value in numbers:
    print(value)

print("new program \n")

menu=[
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","egg","spam","spam","bacon","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        print(f"{meal} as a spam score of {meal.count('spam')}")
