def findLine(prog, target):
    theList = []
    for i in range(len(prog)):    # when prog = ['10 GOTO 20', '20 GOTO 30'], i in range(2)
        theList = (prog[i].split())    # theList = ['10', 'GOTO', '20'] when i = 0 and ['20', 'GOTO', '30'] when i = 1
        if theList[0] == target:    # if the first element of theList, which can either be 10 or 20, eqauls to target, return index
            return i
