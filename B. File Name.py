import re
n = int(input())
s = input()
arr = re.findall(r"x{3,}",s)
c = 0
for i in arr:
    c+=len(i)-2
print(c)