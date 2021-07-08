w = ""
s = input().lower()
for i in s:
    if i == "a" or i=="e" or i=="i" or i=="o" or i=="u" or i == "y":
        continue
    w += '.'+i
print(w)