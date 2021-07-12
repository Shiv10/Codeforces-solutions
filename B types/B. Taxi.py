n = int(input())
a = list(map(int, input().split()))
four = a.count(4)
three = a.count(3)
tow = a.count(2)
one = a.count(1)

c = four + three + (tow//2)
if(one>=three):
    one = one - three
else:
    one = 0

if not (tow%2==0):
    c += 1
    if(one <= 2):
        one = 0
    else:
        one -= 2

if one>0:
    c += one//4
    one = one % 4
    if(one>0):
        c += 1

print(c)
