t=("a","b","c")
print(t)

name="Tim"
age=10

print(name,age,"Python",2020)
print((name,age,"Python",2020))

print("_"*30)

welcome="welcome to my Nightmare","alice Cooper",1975
bad="Bad Company", "bad company", 1974
budgie="Nightflight","Budgie",1981
imelda="More Mayhem","emilda May",2011
metallica="Ride the Lightning","Metallica",1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

# the below will error as tuples are immutable which is its advantage to protect data
# mettalica[0]="Master of Puppets"

mettalica2=list(metallica)
mettalica2[0]="Master Of Puppets"
print(mettalica2)
