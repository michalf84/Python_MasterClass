class Human():
    def __init__(self,name,a,b):
        self.name=name
        self.glowa=Glowa(a,b)
class Glowa():
    def __init__(self,size,color):
        self.size=size
        self.color=color
class Ears():
    def __init__(self):
        self.shape='owal'

michal=Human('michal',1,'d')
print(michal.glowa.color)
