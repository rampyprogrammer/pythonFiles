# # class Myclass:
# #     def __init__(self,items):
# #         self.items=items
    
# #     def __len__(self):
# #         return len(self.items)
    
# # itms=Myclass([1,2,3,4,4])
# # print(len(itms))

# ##__str__

# class Myitems:
#     def __init__(self,items):
#         self.items=items

#     def __getitem__(self,index):
#         return self.items[index]
    

# obj=Myitems([1,2,3,4,5])
# print(obj[2])

class MyList:
    def __init__(self,items):
        self.items=items
    def __setitem__(self,index,value):
         self.items[index]=value

obj=MyList([1,2,3,4,5,6])

obj[2]=1000
print(obj)