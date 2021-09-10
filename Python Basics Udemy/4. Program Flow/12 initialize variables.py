shipping_list=["milk","pasta","eggs","spam","bread"]

item_to_find="albatross"
found_at= None #if not set as none print if not found would give error

for index in range(len(shipping_list)):
    if shipping_list[index]==item_to_find:
        found_at=index
        break
print (f"item found at position {found_at}")

##  EASIER AND BETTER CODE
shipping_list=["milk","pasta","eggs","spam","bread"]
item_to_find="albatross"
found_at=None

if item_to_find in shipping_list:
    found_at=shipping_list.index(item_to_find)
if found_at is not None:
    print(f"item found position: {found_at}")
else:
    print("not found")