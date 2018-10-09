def execute(prog):
    location = 0
    while True:
        if location == len(prog) - 1:    # when index equals to the position of 'LINENUMBER END'
            return 'success'
        
        theList = prog[location].split()    # ['10 GOTO 20'] -> theList = ['10', 'GOTO' '20']
        T = theList[2]    # when theList = ['LINENUMBER GOTO TARGET'], T = TARGET
        previous = theList[0]    # previous = LINENUMBER
        location = findLine(prog, T)    # when prog[i] = ['TARGET GOTO ANOTHER TARGET'], location = index of prog[i]
        theList = prog[location].split()    # New line means theList = ['TARGET', 'GOTO', 'ANOTHER TARGET']
        
        if len(theList) == 3:    # 'LINENUMBER END' has length of 2; when theList does not have END
            present = theList[2]
            if previous == present:    # ['10', 'GOTO', '20'] ['20', 'GOTO', '10']
                return 'infinite loop'
