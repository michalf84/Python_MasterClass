result= True
another_result= result
print(id(result))
print(id(another_result))

print()
result=False
print(id(result))
print()

result="correct"
another_result=result
print(id(result))
print(id(another_result))

result+="ish"
print(id(result))