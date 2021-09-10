import sys

def my_range(n: int):
    print("my range starts")
    start=0
    while start<n:
        print("my range is returning{}".format(start))
        yield start
        start+=1

# the below is generator because of yield that's why order of print is distorted, kyou can read it using next or for
big_range=my_range(5)
print("big range is {} bytes ".format(sys.getsizeof((big_range))))

# create a list containing all the values in big_range
big_list=[]
for x in big_range:
    big_list.append(x)

print("big list is {} bytes ".format(sys.getsizeof((big_list))))

print(big_range)
print(big_list)



print("******")

def my_range2(n: int):
    print("my range starts")
    start=0
    while start<n:
        print("my range is returning{}".format(start))
        yield start
        start+=1
# BECAUSE OF ALL TO ABOVE DON'T ASSIGNE GENERTOR TO VARIABLE!!

a=my_range2(5)
print(next(a))
print(next(a))