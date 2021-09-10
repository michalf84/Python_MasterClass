entries=[1,2,3,4,5]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("iterable with a false value")
entries_with_zero=[1,2,4,5,0]
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))


print("iterable with a false value")
entries_with_null=[]
print("all!!!!: {}".format(all(entries_with_null)))
print("any: {}".format(any(entries_with_null)))