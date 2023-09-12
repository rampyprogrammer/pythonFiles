def isPrime(val,i=2):
    
    if val<2:
        return False
    elif val%i==0:
        return False
    elif val%i!=0:
        return True
    
    isPrime(val,i+1)
def printPrime(start,end):
    count=0
    if start<=end:
        if isPrime(start):
            count+=1
            
            print("count : "+count,start,end=" ")
        printPrime(start+1,end)
start=int(input("enter the lower limit number :"))
end=int(input("enter the upper limit number :"))
printPrime(start,end)

