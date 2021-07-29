def fib(n, d = {}):
    if n in d.keys():
        return d[n]

    if n <= 2:
        return 1

    d[n] = fib(n-1) + fib(n-2)
    return d[n]

n = int(input())
print(fib(n))
