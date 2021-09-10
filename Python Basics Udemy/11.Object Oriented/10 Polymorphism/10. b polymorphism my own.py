class Wing():
    def __init__(self,ratio):
        self.ratio=ratio

    def fly(self):
        if self.ratio>1:
            print(">1")
        elif self.ratio==1:
            print("this is =1")
        else:
            print("other ratio")

class Leg():
    def __init__(self,rozmiar):
        self.rozmiar=rozmiar

class Duck():
    def __init__(self):
        self.wing=Wing(self)
        self.noga=Leg(2)

    def walk(self):
        print("waddle waddle")

    def swim(self):
        print("i can do it")

    def quack(self):
        print("I can quack")
    def fly(self):
        self.wing.fly()

def test_program(x):
    x.walk()
    x.swim()
    x.fly()
    x.quack()

donald=Duck()

print(donald.wing.ratio.noga.rozmiar)
