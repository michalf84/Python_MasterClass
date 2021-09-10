text ="some random text some"

output=[]
for x in text.split():
    output.append(len(x))
print(output)

answer=[len(x) for x in text.split()]
print(answer)

answer=[(x,len(x)) for x in text.split()]
print(answer)

#that removes duplciates due to set
answer={(x,len(x)) for x in text.split()}
print(answer)