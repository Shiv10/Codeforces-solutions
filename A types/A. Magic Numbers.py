s = input()
if(s[0]=="4"):
    print('NO')
    exit()

if("0" in s or "2" in s or "3" in s or "5" in s or "6" in s or "7" in s or "8" in s or "9" in s):
    print("NO")
    exit()

if("444" in s):
    print("NO")
    exit()

print("YES")