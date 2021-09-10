import sys
# !!!! look inot YIELD!!

def my_range(n: int):
    print("my range starts")
    start=0
    while start<n:
        print("my range is returning{}".format(start))
       #returns mulitple values but also exceutes multiple times
        yield start
        start+=1

_=input("line 12")
#big_range=range(1000)
big_range=my_range(5)
_=input("line 15")
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

#create a lsit continin all the values in big_range
big_list=[]

_=input("line 21")

for val in big_range:
    _=input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

print(big_range)
print(big_list)