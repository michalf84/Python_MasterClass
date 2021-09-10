a=12
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
#---------------------------
print()
for i in range(1,4):
    print(i)
print()
#--------------------------
c="we win"
for i in range(0,len(c)):
    print(c[i])
#---------------------------------
print()
d="negative indexing"
print(d)
print(d[-1])

print("print: a[0:3]:",d[0:3])
print("print: a[2:5]:",d[2:5])
print("print: a[2:-3]:",d[2:-3])
print("print: a[:4]:",d[:4])
print("print: a[5:]:",d[5:])
print("print: a[:]:",d[:])
print("print: a[-4:-2]:",d[-4:-2])
print("print: a[-14:6]:",d[-14:6])
print("print: a[0:12:2]:",d[0:12:2])
print("print: a[0::2]:",d[0::2])
print()

nu="9,223;453:432 654,434;321"
separators=nu[1::4]
print(separators)
values="".join(char if char not in separators else " " for char in nu).split()
print([int(val) for val in values])

print()
print("****negative stepping**")
splitback="some text to cliseback"
backwards=splitback[25:0:-1]
print(backwards)
backwards=splitback[25::-1]
print(backwards)
print()


nowy="nowytexta"
print(nowy)
nowy2=nowy[8:2:-2]
print("nowy[8:2:-2]",nowy2)
print("nowy[:-6:-1] ",nowy[:-6:-1])
print("nowy[7:2:-1]: ",nowy[7:2:-1])
print("nowy[-6:] ",nowy[-6:])
print("nowy[:-6] ",nowy[:-6])
print("nowy[:6:-1] ",nowy[:6:-1])
print("nowy[0:-6:-1] ",nowy[0:-6:-1])


