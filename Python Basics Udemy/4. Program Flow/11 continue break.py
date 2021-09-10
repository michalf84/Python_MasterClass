shopping_list=["milk","juice","oranges","bread"]

for item in shopping_list:
    if item !="milk":
        print("buy "+ item)

#   see how milk is skipped from printing
print("*"*10)
for item in shopping_list:
    if item =="milk":
        continue
    print("buy "+ item)

print()
print("*"*10)
for item in shopping_list:
    if item =="juice":
        break
    print("buy "+ item)
