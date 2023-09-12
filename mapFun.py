l1=[1,2,3,4,5,6,7,8,9]
# res=list(map(float,l1))
# print(res)
def Saquare(x):
    return x**2

res=set(map(Saquare,l1))
print(res)
