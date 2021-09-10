sampleText="python is very powerful langea"

vowels=frozenset("aeiou")

finalSet=set(sampleText).difference(vowels)
print(finalSet)

finalList=sorted(finalSet)
print(finalList)