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

# solution 1
for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index]=="spam":
            del meal[index]
    print(meal)

# solution 2
print("OPTION 2")
for meal in menu:
    for item in meal:
        if item!="spam":
            print(item,end= ", ", sep="*")
    print()

print("OPTION 1 enhanced")
# option  (1 enhanced)
for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index]=="spam":
            del meal[index]
    print(", ".join(meal))