print(__file__)
numbers=[1,2,3,4,5,6]

squares=[number**2 for number in range(1,7)]
print(squares)

number=int(input("please enter a number and i will tell you some shit"))
squares=[]
for number in numbers:
    squares.append(number**2)

print(squares)
index_pos=numbers.index(number)
print(squares[index_pos])

#wrong result because number iterates via numbers list
#note that in comprehendion and not for loop the result would be correct

numbers2=[1,2,3,4,5,6]
number2=int(input("enter value"))
squares2=[number2**2 for number2 in numbers2]
print("squares: [{}]".format(squares2))
index_pos=numbers2.index(number2)
print(squares[index_pos])
