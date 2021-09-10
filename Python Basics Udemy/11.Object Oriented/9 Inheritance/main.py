from Player import Player

tim=Player("Tim")

from enemy import Enemy,Troll,Vampire,VampyreKing

random_monster=Enemy("Basic enemy",12,1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll=Troll("Pug")
print("ugly troll - {}".format(ugly_troll))

another_troll=Troll("ug")
print("Another troll - {}".format(another_troll))

brother=Enemy("urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()

vamp=Vampire("vlad")
print(vamp)
vamp.take_damage(1)
print(vamp)

print("*"*100)
# while vamp.alive:
#     if not vamp.dodge():
#         vamp.take_damage(1)
#         print(vamp)

while vamp.alive:
    vamp.take_damage(1)
    print(vamp)

# now we can test vapyreking 