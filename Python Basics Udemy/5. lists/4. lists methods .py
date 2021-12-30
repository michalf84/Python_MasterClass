a=list(range(1,4))
print(a)

even=[2,4,6,8]
odd=[1,3,5,7,9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))
print("index is:",even.index(4))
print()
print(len(even))
print(len(odd))

print("other")
print("mississipi".count("s"))

computer_parts=["computer",
                "monitor",
                "keyboard",
                "mouse"]

computer_parts.append("new product")

for x in computer_parts:
    if x=="monitor":
        print(x)

print(computer_parts[1])

even.extend(odd)
print(even)

a=["michal","ola","costam","jescze","joio","fdsa","aa"]
a.extend("fasola")

# define a first list
course = ['data science', 'machine learning', 'python', 'html', 'big data', 'html' ]
course.reverse()
print("reversed b is :",course)

even.sort()
print(even)
even.sort(reverse=True)
print(even)
# sort does not create a copy of the list but rearranges it. Good for performance as methods copyign list can cause out of memory
# sorted(even)
another_even=even
print(another_even)

computer_parts[3]="trackball"
print(computer_parts)

# note at the vbelow !
computer_parts[3:]="nowe"
print(computer_parts)
computer_parts[1:]=["zmiana"]
print(computer_parts)

print()
data=[4,5,104,105,110,120,130,50,160,170,183,187,188,191,350,360]
del data[0:2]
print(data)
del data[3:]
print(data)

min_value=100
max_value=200

# #IT WON'T WORK AS WE CHANGE LIST thus when we iterate index length changes
for index,value in enumerate(data):
    if(value<min_value) or (value>max_value):
        del data[index]
print(data)

# ----------------------------------------
print()
print("-"*200)
data=[4,5,104,105,110,120,130,50,160,170,183,187,188,191,350,360]
print(data)
# process low vlues in the list assume we have little memory

stop=0

for index,value in enumerate(data):
    if value>=min_value:
        stop=index
        break

print(stop)
del data[:stop]
print(data)

# process high values in the list
start=0
for index in range(len(data)-1,-1,-1):
    if data[index]<=max_value:
        # we have the index of the lat item to keep
        # set start to the position of first
        start=index+1
        break
print(start)
del data[start:]
print(data)

