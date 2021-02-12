import math
t = int(input())

def findFact(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return i
    return n

for _ in range(t):

    n, k = map(int, input().split())
    if n%2 == 0:
        print(n+2*k)
        continue
    print(n+(2*(k-1))+findFact(n))