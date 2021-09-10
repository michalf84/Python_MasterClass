cities=["plocis","warszawa","slask"]

with open("writesample.txt","w") as cityfile:
    for city in cities:
        print(city,file=cityfile)

cities=[]

with open("writesample.txt","r") as city_file:
    for city in city_file:
        cities.append(city.strip('\n')) #to remove end line
print(cities)

for city in cities:
    print(city)

print("*"*59)

with open("imelda3.txt","r") as imelda:
    contents=imelda.readline()
print(contents)

im=eval(contents)
print(im)

title,artist,year,tract=im
print(title)