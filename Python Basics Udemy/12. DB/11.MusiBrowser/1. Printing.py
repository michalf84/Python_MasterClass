# allows to print either to ui or to a file

def print_backwards(*args,file=None):
    for word in args[::-1]:
        print(word[::-1],end=' ', file=file)
    
with open("backwards.txt",'w') as backwards:
    print_backwards("hello","planet","earth","take","me","to","your","leader",file=backwards)


# allows to print either to ui or to a file

def print_backwards1(*args,**kwargs):
    for word in args[::-1]:
        print(word[::-1],end=' ', **kwargs)

with open("backwards2.txt",'w') as backwards2:
    print_backwards("hello","planet","earth","take","me","to","your","leader",file=backwards2)


# fixes issue where we provide to kwargs already provided parameter that would result in crash like 'end'

# def print_backwards2(*args,end=' ',**kwargs):
def print_backwards2(*args,end=' ',**kwargs):
    for word in args[::-1]:
        kwargs.pop('end',None)
        print(word[::-1],end=' ', **kwargs)

with open("backwards2.txt",'w') as backwards2:
    print_backwards("hello","planet","earth","take","me","to","your","leader",file=backwards2)

#note that pipe separator is not dpoalyed

print("hello","planet","earth","take","me","to","your","leader",end='\n',sep='|')
print_backwards2("hello","planet","earth","take","me","to","your","leader",end='\n',sep='|')

#fixing above
print()
print()
def print_backwards2fix(*args,end=' ',**kwargs):
    end_character=kwargs.pop('end','\n')
    sep_character=kwargs.pop('sep',' ')
    for word in args[::-1]:
        print(word[::-1],end=sep_character, **kwargs)
#better to replace it with .join
    print(end=end_character)
#note that pipe separator is not dpoalyed

print("hello","planet","earth","take","me","to","your","leader",end='\n',sep='|')
print_backwards2fix("hello","planet","earth","take","me","to","your","leader",end='\n',sep='|')

