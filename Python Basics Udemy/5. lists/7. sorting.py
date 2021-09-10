pangram="The quick brown box jumps over the lazy dog"

letter=sorted(pangram)
print(letter)

numbers=[2.3,4.5,3.1,9.2,1.6]
sorted_numbers=sorted(numbers)
print(sorted_numbers)
print(numbers)
# sort does not create a copy of the list but rearranges it. Good for performance as methods copyign list can cause out of memory
numbers.sort()
print(numbers)

another_sorted_numbers=numbers.sort()
print(numbers)
print(another_sorted_numbers)

missing_letter=sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)

#case insesitive sorting
missing_letter=sorted("The quick brown fox jumped over the lazy dog",key=str.casefold)
print(missing_letter)

names=["Graham",
       "John",
       "terry",
       "eric",
       "Terry",
       "michael"]
names.sort(key=str.casefold)
print(names)

print()
empty_list=[]
even=[2,4,6,8]
odd=[1,3,5,7,9]

numbers=even+odd
print(numbers)

sorted_numbers=sorted(numbers)
print(sorted_numbers)

digits=sorted("432747")
print(digits)
# new list created new copy
more_numbers=list("432747")
print(digits)
print(numbers is more_numbers)

more_numbers=digits[:]
print(more_numbers)

print()
even_more=numbers.copy()
print(even_more)