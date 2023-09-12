#hirarical inhiretence
class Animal:
    def __init__(self,color,name):
      self.color=color
      self.name=name
        

    def Eating(self):
        print(f"{self.name} will eat food 2 times a day")

class Dog(Animal):
    def __init__(self,runspeed,color,name):
      super().__init__(color,name)
      self.runspeed=runspeed

    def run(self):
      print(f"a {self.name} can run in the speed of {self.runspeed}km/hr")

class Fish(Animal):
    def __init__(self,swimSpeed,name,color):
      super().__init__(name,color)
      self.swimSpeed=swimSpeed

    def Swim(self):
       print(f"{self.name} can swim in the speed of {self.swimSpeed}km/hr")



obj=Dog(40,'black','munna')

obj.Eating()
obj.run()

obj2=Fish(34,"yellow Blue","alice")
obj2.Eating()
obj2.Swim()

##multiple inhiretence
class A:
    def Method(self):
        print("this is method 1 from a class A")

class B:
    def Method(self):
        print("this is a method from class B ")

class C(B,A):
    pass

obj=C()
obj.Method()