class Enemy:
#or class Enemy(object)
    def __init__(self, name="Enemy",hit_points=0,lives=1):
        self._name=name
        self._hit_points=hit_points
        self._lives=lives
        self.alive=True

    def take_damage(self,damage):
        remaining_points= self._hit_points - damage
        if remaining_points>=0:
            self._hit_points=remaining_points
            print("I took {} point damage and have{} left".format(damage, self._hit_points))
        else:
            self._lives-=1
            if self._lives>0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self.alive=False

    def __str__(self):
        return "_name: {0._name},Lives{0._lives}, Hit points:{0._hit_points}".format(self)

#class Troll(Enemy): #inheritance
#   pass # to allow the class with no initation to work


class Troll(Enemy): #inheritance
   # pass # to allow the class with no initation to work
   #def __init__(self,_name):
        #the below must be added as _name would not be initiated and others,
        #it is because we initiated new class thus need to explicitly call enemy superclass
        #Enemy.__init__(self,_name=_name,_lives=1,_hit_points=23)
        #algernative to above below note that we removed _name from main init method, we removed self from Enemy.__init
    def __init__(self,name):
        super().__init__(name=name,lives=1,hit_points=23)

    def grunt(self):
        print("Me {0._name} . {0._name} stomp you ".format(self))

class Vampire(Enemy):
    def __init__(self,name):
        super().__init__(name=name,lives=3,hit_points=12)

    #override method of enemy
    def dodge(self):
        import random
        if random.randint(1,3)==3:
            print("***** {0._name} doges ****".format(self))
            return True
        else:
            return False

    def take_damage(self,damage):
        if not self.dodge():
            super().take_damage(damage=damage)


class VampyreKing(Vampire):

    def __init__(self,name):
        super().__init__(name)
        self._hit_points=140
        
    def take_damage(self,damage):
        super().take_damage(damage//4)