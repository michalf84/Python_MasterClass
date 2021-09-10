for i in range (1,13):
    print("No.{0} squared is {1} and cubed is {2}".format(i,i**2,i**3))

print()
print()
#apply formatting
for i in range (1,13):
    print("No.{0:2} squared is {1:4} and cubed is {2:4}".format(i,i**2,i**3))

print()
print()
#apply formatting
for i in range (1,13):
    print("No.{0:2} squared is {1:<3} and cubed is {2:^4}".format(i,i**2,i**3))

print()
print("pi is approx {0:12}".format(22/7))
print("pi is approx {0:12f}".format(22/7))
print("pi is approx {0:12.5f}".format(22/7))
print("pi is approx {0:52.50f}".format(22/7))
print("pi is approx {0:62.50f}".format(22/7))
print("pi is approx {0:72.50f}".format(22/7))

#new method
print()
x="some text is : "
age=24

print(x+f" and age is:{age}"+" old")

print(f"pi is approx {22/7}")
print(f"pi is approx {22/7:12.7f}")

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
