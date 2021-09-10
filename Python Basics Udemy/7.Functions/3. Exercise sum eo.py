def sum_eo(n,t):
    i=0
    j=0
    if t=='e':
        for x in range(2,n,2):
           i+=x
        return i
    elif t=="o":
        for x in range(1,n,2):
            j+=x
        return j
    else:
        return -1
           
print(sum_eo(7,"o"))