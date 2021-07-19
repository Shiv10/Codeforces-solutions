n, m, a, b = map(int, input().split())
s = n*a
c = ((n//m)*b) + min(((n%m)*a),b)
print(min(s,c))