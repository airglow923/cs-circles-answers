def getBASIC():
    theList = []
    
    while True:
        userInput = input()    # 10 GOTO 20
        statement = userInput.split()    # statement = ['10', 'GOTO', '20]
        theList.append(userInput)    # theList = ['10', 'GOTO', '20']

        if statement[1] == 'END':    # ['LINENUMBER', 'END']
            return theList
