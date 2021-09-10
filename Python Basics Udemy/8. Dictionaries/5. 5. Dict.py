fruit={"orange":"a sweet fruit",
       "apple":"red fruit",
       "lemon":"yellow citrus fruint",
       "grape":"a msall sweet fruitn growning in branches"}
print(fruit)

veg={"cabbage":"every child fabourite",
     "sprouts":"mmm, lovely",
     "spinach":"can i have some more fruit please"}
print(veg)

veg.update(fruit)

print(veg)
print(fruit.update(veg))
print(fruit)
print()

nice_and_nasty=fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
