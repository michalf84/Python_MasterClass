# look at underscores in python video informative

import Blackjack_17

# # will get error can't import globals like that
# for x in globals():
#     print(x)

g=sorted(globals())
for x in g:
    print(x)
print("*"*20)
print(__name__)
Blackjack_17.play()
print(Blackjack_17.cards)