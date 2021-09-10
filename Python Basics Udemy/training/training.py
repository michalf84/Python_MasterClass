class Parent():
    age=0
    def __init__(self,name):
        self.name=name
    def spit(self):
        print("I can spit")
class Child(Parent):
    def __init__(self,parentname):
        self.parentname=parentname
        super().__init__("jerzy")

michal=Parent("michal")
michal.age=3
print(michal.age)

ola=Parent("Ola")
print(ola.age)

ines=Child("michal")
print(ines.age)


print(ines.spit())
