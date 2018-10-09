def execute(prog):
    location = 0
    while True:
        if location == len(prog) - 1:
            return 'success'
        
        theList = prog[location].split()
        T = theList[2]
        previous = theList[0]
        location = findLine(prog, T)
        theList = prog[location].split()
        
        if len(theList) == 3:    # 'LINENUMBER END' has length of 2
            present = theList[2]
            if previous == present:
                return 'infinite loop'
