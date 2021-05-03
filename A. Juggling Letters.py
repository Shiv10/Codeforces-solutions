dic = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
t = int(input())

for i in range(t):
    d = dic
    flag = True
    n = int(input())
    a = []
    for i in range(n):
        a.append(input())

    for i in a:
        for j in i:
            d[j]+=1
    
    for i in dict.keys(d):
        if not (d[i]%n==0):
            print("NO")
            flag = False
            break
    
    if(flag):
        print("YES")
        
    for i in dict.keys(d):
        d[i] = 0
    