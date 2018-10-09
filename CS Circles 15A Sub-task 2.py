def findLine(prog, target):
    theList = []
    for i in range(len(prog)):
        theList = (prog[i].split())
        if theList[0] == target:
            return i
