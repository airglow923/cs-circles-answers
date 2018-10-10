def check(S):
    userInput = S
    List = list(userInput)
   
    userInput = S.replace(' ', '')
   
    if len(userInput) != 16:
        return False
   
    for i in range(len(List)):
        i = int(i)
        
        if i == 4 or i == 9 or i == 14:
            if List[i] != ' ' and List[i] != ' ' and List[i] != ' ':
                return False
         
        elif not List[i].isdigit():
            return False
   
    theList = list(userInput)
    a = 0
   
    for i in range(len(theList)):
        a += int(theList[i])
   
    if a % 10 == 0:
        return True
   
    else:
        return False
