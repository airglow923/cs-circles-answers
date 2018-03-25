import math
L = float(input())
A = float(input())
for T in range(0, 10):
   print(L*math.cos(A*math.cos(T*math.sqrt(9.8/L)))-L*math.cos(A))
