import     duck7battributeeeror as ducks
#duck7

# flock=duck7.Flock()
# donald=duck7.Duck()
# daisy=duck7.Duck()
# duck3=duck7.Duck()
# duck4=duck7.Duck()
# duck5=duck7.Duck()
# duck6=duck7.Duck()
# duck7=duck7.Duck()
# #thanks to description in duck7 error is verfy specific: AttributeError: 'Duck' object has no attribute 'Penguin'
# percy=duck7.Penguin()
#
# flock.add_duck(donald)
# flock.add_duck(daisy)
# flock.add_duck(duck3)
# flock.add_duck(duck4)
# flock.add_duck(duck5)
# flock.add_duck(duck6)
# flock.add_duck(duck7)
# flock.add_duck(percy)
#
# flock.migrate()

flock = ducks.Flock()
donald = ducks.Duck()
daisy = ducks.Duck()
duck3 = ducks.Duck()
duck4 = ducks.Duck()
duck5 = ducks.Duck()
duck6 = ducks.Duck()
duck7 = ducks.Duck()
percy = ducks.Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy)
flock.add_duck(duck5)
flock.add_duck(duck6)
flock.add_duck(duck7)

flock.migrate()