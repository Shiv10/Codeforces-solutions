a, n = map(int, input().split())
s = input()
for i in range(n):
    s = s.replace("BG", "GB")

print(s)