n = int(input())
c = 1
i = 1
n = n-c
while n>0:
    i+=1
    c = (i*(i+1))//2
    n-=c

if n<0:
    print(i-1)
else:
    print(i)