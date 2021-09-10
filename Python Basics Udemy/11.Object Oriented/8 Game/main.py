import Player
#lub from player import Player

tim=Player.Player("tim")

print(tim.name)
print(tim.lives1)
tim.lives1-=1
print(tim.lives1)

#  You would do the below in Jave and C++ but it is not needed in python
# print(tim.get_name())
# tim.set_lives(300)

tim.lives-=1
print(tim)
tim.lives-=1
print(tim)
tim.lives-=1
print(tim)
tim.lives-=1
print(tim)

#new setter mehod

tim.score=500
print(tim)