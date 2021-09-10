a=4
b=3

print(a+b)
print(a.__add__(b))

class Kettle(object):

    power_source="electricity"

    def __init__(self,make,price):
        self.make=make
        self.price=price
        self.on=False

    def switch_on(self):
        self.on=True


kenwood=Kettle("kenwood",8.99)
print(kenwood.make)
print(kenwood.price)

hamilton=Kettle("Hamilton",15.33)

print("models are {},{},{}".format(kenwood.make,kenwood.price,hamilton.make))
print()

print("Models:{0.make}={0.price},{1.make}={1.price}".format(kenwood,hamilton))
print()

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print("***")
Kettle.switch_on((kenwood))
print(kenwood.on)
kenwood.switch_on()
print(kenwood.on)

print("*"*80)

kenwood.power=1.5
print(kenwood.power)

print(Kettle.power_source)
print(kenwood.power_source)

print(Kettle.__dict__)
print('-----------')
print(kenwood.__dict__)
print()
kenwood.power_source="gas"
print(kenwood.__dict__)