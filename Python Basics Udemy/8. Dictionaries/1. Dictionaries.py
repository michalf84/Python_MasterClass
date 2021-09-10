fruit={"orange":"a sweet fruit",
       "apple":"red fruit",
       "lemon":"yellow citrus fruint",
       "grape":"a msall sweet fruitn growning in branches"}

print(fruit)
print()

print(fruit["lemon"])

bike = {"make": "Honda", "model": "250 dream", "colour": "red", "engine_size": 250}
print(bike["engine_size"])
print(bike["colour"])

fruit["nowy"]="newly added fruint"
print(fruit["nowy"])
fruit["nowy"]="changed overrriden value"
print(fruit["nowy"])

print()
del fruit["lemon"]
print(fruit)

print()

while True:
    dict_key=input("enter fruit")
    if dict_key=="quit":
        break
    if dict_key in fruit:
        description=fruit.get(dict_key)
        print(description)
    else:
        print("don't have it")


#note that .get retursn none when no result found no error