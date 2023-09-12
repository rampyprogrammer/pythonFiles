# def my_gen():
#     n=2
#     while True:
#         yield n
#         n+=2
# gen=my_gen()

# for i in range(100):
#     print(next(gen))

def FiboNaci():
    a,b=0,1
    while True:
        yield a
        a,b=b,b+a

fib=FiboNaci()

for i in range(10):
    print(next(fib))