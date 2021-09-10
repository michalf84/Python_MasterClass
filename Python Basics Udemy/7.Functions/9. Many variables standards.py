def func(p1,p2,*args,k,**kwargs):
    print(f"positional or keywork:....{p1}{p2}")
    print(f"var positional(*args):... {args}")
    print(f"keyword:... {k}")
    print(f"var kyword:  ... {kwargs}")

func(1,2,3,4,5,9,k=6,key1=7, key2=8)



def t(**kwargs):
    for key, value in kwargs.items():
        print(key)

t(a='1',b=5)

