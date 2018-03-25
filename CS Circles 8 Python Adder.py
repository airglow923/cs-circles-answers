S = input()
for position in range(0, len(S)):
   if S[position] == '+':       #find where the numbers are split by the plus sign
      str1 = int(S[0:position]) #turns str1 into number1
      str2 = int(S[(position+1):len(S)])  #turns str2 into number2
      print(str1 + str2)
