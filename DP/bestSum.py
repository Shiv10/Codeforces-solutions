def bestSum(n, a, d = {}):
    if n in d.keys():
        return d[n]
    
    if n == 0:
        return []
    if n<0:
        return -1
    
    short = -1
    for i in a:
        rem = n - i
        res = bestSum(rem, a, d)
        if isinstance(res, list):
            res.append(i)
            if (short == -1 or len(short)>len(res)):
                short = res
    d[n] = short 
    return short

n = int(input())
a = list(map(int, input().split()))
print(bestSum(n,a))

