n = int(input())
for a in range(1, n + 1):  # substitute all integers within the range of input
   for b in range(1, n + 1):  # substitue all integers within the range of input
      if a * b == n:
         print (a, 'times', b, 'equals', n)
