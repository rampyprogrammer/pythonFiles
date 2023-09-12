# class Overloading:
#     def Sum(self,a,b):
#         return a+b
#     def Sum(self,a,b,c):
#         return a+b+c
#     def Sum(self,a,b,c,d):
#         return a+b+c+d
# obj=Overloading()
# print(obj.Sum(1,2,3))


#in python method over loading does not support
#to achieve this we can use variable arguments
def Sum(*arg):
    sum=0
    for i in arg:
        sum+=i
    return sum
res=Sum(10,20,30,40,50,60,70)
print(res)