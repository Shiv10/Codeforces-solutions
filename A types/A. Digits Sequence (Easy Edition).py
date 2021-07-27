k = int(input())
n = 0
s = ""
for i in range(1,k+1):
    n+=1
    s = s+str(n)
    i+= len(str(n))

print(s[k-1])
    