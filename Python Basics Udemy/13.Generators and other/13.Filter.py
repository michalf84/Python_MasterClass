import timeit
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

for meal in menu:
    if "spam" not in meal:
        print(meal)
print("-" * 40)

def smapless_comp():
    meals = [meal for meal in menu if "spam" not in meal]
    return meals

print("-" * 40)

def not_spam(meal_list:list):
    return "smpam" not in meal_list
def smapless_comp2():
    meals = [meal for meal in menu if not_spam(meal)]
    return meals
def smapless_filter():
    smapless_meals=list(filter(not_spam,menu))
    return smapless_meals

if __name__=='__main__':
    print(smapless_comp())
    print(smapless_comp2())
    print(smapless_filter())
    print(timeit.timeit(smapless_comp,number=100000))
    print(timeit.timeit(smapless_comp2,number=100000))
    print(timeit.timeit(smapless_filter,number=100000))