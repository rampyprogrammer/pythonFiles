def My_decorator(fun):
    def Wrapper():
        print("something is heppening before calling the function")
        fun()
        print("somthing is happened after calling the function")
    return Wrapper

@My_decorator
def saySomthing():
    print("hello world !")

saySomthing()