def longestSubString(a, b):
  if (len(a) == 0 or len(b) == 0):
    return "No substring"

  l = len(a)
  t = len(b)

  d = [[0 for i in range(t+1)] for j in range(l+1)]
  ml = 0
  row, col = 0, 0

  for i in range(l+1):
    for j in range(t+1):
      if i == 0 or j == 0:
        d[i][j] = 0
        continue

      if a[i-1] == b[j-1]:
        d[i][j] = d[i-1][j-1] + 1
        if d[i][j] > ml:
          ml = d[i][j]
          row = i
          col = j
        continue

      d[i][j] = 0

  if ml==0:
    return "No substring"


  w=""

  while(d[row][col]!=0):
    w+= a[row-1]
    row-=1
    col-=1
  return w[::-1]

a = input()
b = input()
print(longestSubString(a,b))