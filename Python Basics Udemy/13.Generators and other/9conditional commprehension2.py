menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
meals=[]
for meal in menu:
    if "spam" not in meal:
        print(meal)
        meals.append(meal)
    else:
        meals.append("a meal was kidnapped")


meals=[meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

x=12
expression="thelve" if x==12 else "unknown"
print(expression)

meals=[meal if "spam" not in meal else "meal was skipped" for meal in menu]
print(meals)

print("*"*50)
print(menu)
print("-"*50)
for meal in menu:
    print(meal,"contans chcieken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")