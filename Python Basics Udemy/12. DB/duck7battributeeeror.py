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

class Mallard(Duck):
    pass

class Flock(object):
    def __init__(self):
        self.flock=[]
#by adding descirpiton eeror message in migraiton file will e specific
   #def add_duck(self,duck) OLD
    def add_duck(self,duck: Duck)-> None:
    #note at this info annotation
    #the below if and self indented removes error
        #if type(duck) is Duck:
    #these are not pythonic
      #   if isinstance(duck,Duck):
    #pythonic is belos
        fly_method=getattr(duck,'fly',None)
        if callable(fly_method):
            self.flock.append(duck)

    def migrate(self):
        problem=None
        for duck in self.flock:
            try:
                duck.fly()
                #handled to migrate what we can and error what we can't
            except AttributeError as e:
                print("one duk donw")
                problem=e
                #raise
        if problem:
            raise problem
if __name__=='__main__':
    donald=Duck()
    donald.fly()