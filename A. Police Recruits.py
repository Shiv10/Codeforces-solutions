n = int(input())
a = list(map(int, input().split()))
c = 0
ct = 0
for i in a:
    if(i<0):
        if(c+i<0):
            ct+=1
        else:
            c+=i
    else:
        c+=i
print(ct)