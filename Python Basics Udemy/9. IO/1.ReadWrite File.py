# jabber=open("sample.txt","r")
#
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line,end='' ) #end prevents empty line
# jabber.close()

# new option clsoes file automatically

with open("sample.txt","r") as jabber:
    for line in jabber:
        if "jabberwock" in line.lower():
            print(line,end='' ) #end prevents empty line
print()

with open("sample.txt","r") as jabber:
    line =jabber.readline()
    while line:
            print(line,end='' ) #end prevents empty line
            line=jabber.readline()

print("*"*20)

with open("sample.txt","r") as jabber:
    lines =jabber.readlines()
print(lines)

for line in lines:
    print(line,end='')