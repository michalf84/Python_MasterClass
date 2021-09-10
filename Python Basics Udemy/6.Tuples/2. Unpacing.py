a=b=c=d=e=f=42
print(c)

x,y,z=1,2,76
print(x)
print(y)
print(z)

print("unpacking a tuple")
data=1,2,76 #data represents tuple
x,y,z=data #these are not tuples but variables
print(x)
print(y)
print(z)

print("unpacking list")
data_list=[12,13,14]
p,q,r=data_list
print(p)

for t in enumerate("abcdefgh"):
    print(t)

index,character=(0,"a")
print(index)
print(character)

