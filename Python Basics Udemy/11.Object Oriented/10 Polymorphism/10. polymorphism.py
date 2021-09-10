class Wing(object):
    def __init__(self,ratio):
        self.ratio=ratio

    def fly(self):
        if self.ratio>1:
            print("wwee this is fun")
        elif self.ratio==1:
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

class Penguin(object):

    def walk(self):
        print("waddle waddle I waddle too")

    def swim(self):
        print("come on in but its a bit chilly this far south")

    def quack(self):
        print("are you avin a larf? I m a penguin")

def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()
print("*********************")

#to make sure if the main code if duck polymporphoism file is imported
if __name__=='__main__':
    donald=Duck()
    donald.fly()
    test_duck(donald)

    percy=Penguin()
    test_duck(percy)