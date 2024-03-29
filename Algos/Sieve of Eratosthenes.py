def sieveOfEratosthenes(n):
	prime = [True]*(n+1)
	p = 2
	while (p * p <= n):
		if prime[p]:
			for i in range(p * p, n+1, p):
				prime[i] = False
		p += 1
	for p in range(2, n+1):
		if prime[p]:
			print(p)

n = int(input())
sieveOfEratosthenes(n)
