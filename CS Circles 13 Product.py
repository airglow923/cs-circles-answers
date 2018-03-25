def prod(L):
   a = 1
   for i in range(0, len(L)): # Computing product of the numbers in the list using range    
      a *= L[i]
   return a

def prod(L):
   a = 1
   for i in L: # Computing product of the numbers in the list without using range
      a *= i
   return a
