import math
def checkPrime(n):
    if n<2:
        return False
    if n%2==0:
        return n==2
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i==0:
            return False
    return True

n = int(input())
c = n
if checkPrime(n):
    c+=1
    print(c)
    exit()
while n>1:
    s = 1
    for i in range(2,n//2+1):
        if n%i==0:
            s = i
            n=n//i
            break
    if s==1:
        c+=1
        break
    c+=n
print(c)
