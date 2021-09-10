shopping_list=["milk","soap","glue"]
another_list=shopping_list
print(id(shopping_list))
print(id(another_list))

print()
shopping_list+=["cookies"]
print(id(shopping_list))
print(another_list)
print(shopping_list)

print()
another_list+=["bike**"]
print(another_list)
print(shopping_list)
print(id(shopping_list))
print(id(another_list))