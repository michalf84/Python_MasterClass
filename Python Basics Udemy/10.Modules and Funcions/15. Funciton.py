def python_food():
    print("spam")

python_food()

print()
print(python_food())

def python_food():
    width=80
    text="span and eggs"
    left_margin=(width-len(text))//2
    print(" "*left_margin,text)

print(python_food())

def centre_text(text):
    width=80
    left_margin=(width-len(text))//2
    print(" "*left_margin,text)

centre_text("costam")
centre_text("other informitin is eggs")


def centre_text2(*args,end='\n',file=None,flush=False):
    text=""
    for arg in args:
        text+=str(arg)+" "
    width=80
    left_margin=(width-len(text))//2
    print(" "*left_margin,text,end=end,file=file,flush=flush)

centre_text("costam")
centre_text("other informitin is eggs")

centre_text2(("mich","ol","in","mi"))

print("*"*30)

with open("centred",mode='w') as centered_file:
    centre_text2("blalbla",file=centered_file)
    centre_text2("naortheorextr",file=centered_file)
print()
def centre_text3(*args,sep=' ',end='\n',file=None,flush=False):
    text=""
    for arg in args:
        text+=str(arg)+" "
    width=80
    left_margin=(width-len(text))//2
    return " "*left_margin,text

with open("centred2",mode='w') as menu:
    a=(centre_text3("first","second",3,4,"spam",sep=":"))
    print(a,file=menu)