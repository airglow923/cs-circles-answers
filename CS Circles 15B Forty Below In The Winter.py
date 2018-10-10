userInput = input()
theList = list(userInput)

if theList[len(theList) - 1] == 'C':
    theList.pop(len(theList) - 1)
    degrees = float(''.join(theList))
    f = degrees * 9 / 5 + 32
    print(str(f) + 'F')

elif theList[len(theList) - 1] == 'F':
    theList.pop(len(theList) - 1)
    degrees = float(''.join(theList))
    c = (degrees - 32) * 5 / 9
    print(str(f) + 'C')
