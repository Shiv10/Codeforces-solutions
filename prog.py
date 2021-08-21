def allConstruct(n, a):

    if n == 0:
        return [[]]
    if n < 0:
        return -1

    result = []

    for i in range(len(a)):
        res = allConstruct(n-a[i], a)
        if isinstance(res, list):
            for j in res:
                j.append(a[i])
                result.append(j)
    return result
        

def solution(a, f, m):
    n = len(a)
    n += f
    total = m*n
    s = sum(a)
    left = total - s
    if left > f*6 or left<1:
        return [0]

    res = allConstruct(left, [1,2,3,4,5,6])

    for i in res:
        if len(i)==f:
            return i

print(solution([1, 5, 6], 4, 3))

