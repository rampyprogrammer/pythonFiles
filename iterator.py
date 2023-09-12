class MyIterator:
    def __init__(self,data):
        self.data=data
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.index<len(self.data):
            res=self.data[self.index]
            self.index+=1
            return res
        else:
            raise StopIteration
obj=MyIterator([1,2,3,4,5,6])

for i in obj:
    print(i)