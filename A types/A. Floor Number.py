t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    c = 0
    while True:
        if n<=((c*x)+2):
            print(c+1)
            break
        c+=1
    
