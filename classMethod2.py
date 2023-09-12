class Student:
    rollNo=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        

    def Std_Details(self):
        print(f"""
            name : {self.name}
            age  : {self.age}
            RollNO :{Student.rollNo}""")

    @classmethod
    def std(cls,name,age):
        cls.rollNo+=1
        return cls(name,age)
    
obj=Student.std("ram",22)
obj.Std_Details()

obj1=Student.std("ramakrishna",23)
obj1.Std_Details()