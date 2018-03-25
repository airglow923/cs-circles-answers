width = int(input())
counter = 0
while True:
   a = input()   
   L = len(a)
   b = (width-L) // 2
   c = b
   if ((width-L) % 2) != 0:
      b = b + 1
   if a == 'END':
      break
   print('.' * b + a + '.' * c)
