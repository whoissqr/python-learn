# delete the prime numbers between 0 -100
# i.e. print the composite numbers between 0-100

def printIfPrime():
    L=range(101)  
    print filter(is_prime, L)
    
    
def is_prime(N):
    if((N==0) or (N==1)):
        return False
    if(N==2):
       return True
    
    nums=range(N)[2:]
    for n in nums:
        if(N%n==0):
            return False
        else:
            continue
    return True

printIfPrime()


