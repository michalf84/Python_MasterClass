albums="welcome to my Nightmare","alice Cooper",1975
bad="Bad Company", "bad company", 1974
budgie="Nightflight","Budgie",1981
imelda="More Mayhem","emilda May",2011
metallica="Ride the Lightning","Metallica",1984

title,artist,year=metallica
print(title)
print(artist)
print(year)

albums = [("welcome to my Nightmare", "alice Cooper", 1975),
           ("Bad Company", "bad company", 1974),
            ("Nightflight", "Budgie", 1981),
             ("More Mayhem", "emilda May", 2011),
              ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))
print(albums)
print(albums[0][1])

for album in albums:
    print(f"Album:{album[0]}, Artist:{album[1]}, Year:{album[2]}")

# unpacking 1
print("****unpacked 1***")
for name,artist,year in albums:
    print(f"Album:{name}, Artist:{artist}, Year:{year}")
# unpacking 2
print("****unpacked 2***")
for album in albums:
    name,artist,year=album
    print(f"Album:{name}, Artist:{artist}, Year:{year}")

# see the difference with nr of variables

da=[("micha","12"),
    ("mart","32"),
    ]


for name in da:
    print(name)
for name,age in da:
    print(name,age)

a=[("mic","234"),("ola","123")]

print()
for name in a:
    n,y=name
    print(y)

da
