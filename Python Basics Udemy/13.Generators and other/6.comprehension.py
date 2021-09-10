print(__file__)
numbers=[1,2,3,4,5,6]

squares=[]

for number in numbers:
    squares.append(number**2)
print(squares)

squares2=[]
squares2=[number**2 for number in numbers]
print(squares2)

text="what have the romans ever done for us?"
words=[word.upper() for word in text.split(' ')]
print(words)

# dont do the below it is lesss eficient
lc_words=[word for word in text.split(' ')]
print(lc_words)

#use instead
lc_words=text.split(' ')
print(lc_words)

