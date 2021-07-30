def targetSum(n, a, d={}):
    if n in d.keys():
        return d[n]
    if n == 0:
        return []
    if n < 0:
        return -1
    
    for i in a:
        rem = n - i
        res = targetSum(rem, a, d)
        if res != -1:
            if isinstance(res, list):
                res.append(i)
                d[n] = res
                return res    
    return -1

n = int(input())
a = list(map(int, input().split()))
print(targetSum(n, a))