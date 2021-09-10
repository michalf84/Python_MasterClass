panagram="the quick brown fox jumps over the lazy dog"

words=panagram.split()
print(words)


numbers="9,223,254,234,556,247 "
print(numbers.split(","))
print("\n")


another="".join(char if char not in "," else " " for char in numbers)
print(another)

another2="".join(char if char not in "," else " " for char in numbers).split()
print("another is:",another2)

# it replaces , with space and then during joining adds following space and split removes it and divides into smaller blocks
another3=" ".join(char if char not in "," else " " for char in numbers).split()
print("another is:",another3)


for index in range(8,-1,-3):
    print(index)

# change number to in option 1 another is to append to new list you know how to do it
print("\n Exercise**")
for index in range(len(another2)):
    another2[index]=int(another2[index])
print(another2)




