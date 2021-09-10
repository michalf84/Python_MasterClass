age=12

if age>=16 or age<=16:
    print("costam")
if age in (12,14):
    print("ok")

print("*"*30)

parrot="norwegian blue"

for character in parrot:
    print(character)
#------------------------------
number="9,123;342:433 423,242;324"
separators=""
for char in number:
    if not char.isnumeric():
        separators=separators+char
print(separators)

values="".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))

print("*********sample 2******")
sam="123.312;423.324;421"
sep=""

for x in sam:
    if not x.isnumeric():
        sep+=x
print(sep)
val= "".join(x if not x in sep else " " for x in sam).split()
print(val)