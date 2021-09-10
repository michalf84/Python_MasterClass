# sets are unique

farm_animals={"sheep","cow","hen"}
print(farm_animals)

for animal in farm_animals:
    print(animal)

wild_animals=set(["sheep","cow","hen"])
print(wild_animals)

farm_animals.add("horse")
wild_animals.add("hores")

squares=set(range(0,20,3))
print(squares)

even= set(range(0,40,2))
print(even)
print(len(even))

squares_tuple=(4,6,9,16,25)
squares=set(squares_tuple)
print(squares)
print(len(squares))

print(even.union(squares))
print(len(even.union(squares)))

print("-"*40)

print(even.intersection((squares)))
print(squares.difference((even)))
print(squares-even)

print("="*40)
print(sorted(even))
print(squares)
even.difference_update(squares)
print(sorted(even))

print("symmetric even minus squares")
print(sorted(even.symmetric_difference((squares))))

print()
print(squares)
squares.discard(4)
squares.remove(16)
squares.discard(8)  # no error does noting
print(squares)
# squares.remove(8) # error

#
# try:
#     squares.remove(8)
# except KeyError:
#     print("the item 8 is not member of set")

if squares.issubset(even):
    print("quares is a subest of even")
if even.issubset(squares):
    print("quares is a subest of even")

even=frozenset(range(0,100,2))
print(even)
#even.add(3) error