# class Myclass:
#     rollNo=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         Myclass.rollNo+=1

#     @classmethod
#     def Roll(cls):
#         print(f"          stdcount :{cls.rollNo}")

#     def Std_details(self):
#         print(f"""
#                name :{self.name}
#                age :{self.age}""")
# obj=Myclass("ram",22)
# obj.Roll()
# obj.Std_details()

# obj2=Myclass("rakesh",22)
# obj2.Roll()
# obj2.Std_details()

# obj3=Myclass("vishnu",22)
# obj3.Roll()
# obj3.Std_details()

class MYclass:
    count=0
    def __init__(self,value):
        self.value=value

    @classmethod
    def method(cls,v1,v2):
        #modifying the class variable inside a class method
        cls.count+=1
        return cls(v1+v2)
    
obj1=MYclass.method(10,30)
print(obj1.value)
print(MYclass.count)
