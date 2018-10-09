def getBASIC():
    theList = []
    
    while True:
        userInput = input()
        statement = userInput.split()
        theList.append(userInput)

        if statement[1] == 'END':
            return theList
