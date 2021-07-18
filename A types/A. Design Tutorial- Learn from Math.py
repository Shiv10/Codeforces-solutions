def isPrime(n):
    c=0
    for i in range(1,n):
        if n%i==0:
            c+=1
    return c==1
n = int(input())
a = 8
b = n-a
if(isPrime(b)):
    b-=1
    a+=1
print(str(a)+" "+str(b))