sel=[]
entered=""
print(" enter 3 values separated by coma")

entered=input()

sel=entered.split(",")
print(sel)

int_val=[]

for x in sel:
    int_val.append(int(x))
print(int_val)

a,b,c=int_val
result=a+b-c
print(a)
print(b)
print(result)