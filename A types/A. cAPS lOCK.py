s = input()
f = False
for i in s[1:]:
    if i.islower():
        f = True
        break

if f:
    print(s)
    exit()

w = ""
for i in s:
    if i.isupper():
        w = w+i.lower()
    else:
        w = w+i.upper()

print(w)