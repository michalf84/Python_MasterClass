class Wing(object):
    def __init__(self,ratio):
        self.ratio=ratio

    def fly(self):
        if self.ratio>1:
            print("wwee this is fun")
        elif self.ration==1:
            print("tjhis is hard work bu tim flying")
        else:
            print("i think i will just walk")



class Duck(object):
    # composition attribute has object wing
    def __init__(self):
        self._wing=Wing(1.8)

    def walk(self):
        print("waddle waddle waddle")

    def swim(self):
        print("come on it the weather is lovely")

    def quack(self):
        print("quack quack")

    def fly(self):
        self._wing.fly()
        print("it is fun")

class Penguin(object):

    def walk(self):
        print("waddle waddle I waddle too")

    def swim(self):
        print("come on in but its a bit chilly this far south")

    def quack(self):
        print("are you avin a larf? I m a penguin")

class Flock(object):
    def __init__(self):
        self.flock=[]
#by adding descirpiton eeror message in migraiton file will e specific
   #def add_duck(self,duck) OLD
    def add_duck(self,duck: Duck)-> None:
    #note at this info annotation
        self.flock.append(duck)

    def migrate(self):
        for duck in self.flock:
            duck.fly()

if __name__=='__main__':
    donald=Duck()
    donald.fly()