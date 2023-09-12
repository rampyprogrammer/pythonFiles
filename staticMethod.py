class Myclass:
    age=34
    def __init__(self,name):
        self.name=name


    @staticmethod
    def add(x,y):
        print(Myclass.age)
        return x+y
    
    @staticmethod
    def multi(a,b):
        return a*b
    
# res=Myclass.add(10,20)
# print(res)
# res1=Myclass.multi(10,2)
# print(res1)
obj=Myclass("ram")
print(obj.add(10,20))
