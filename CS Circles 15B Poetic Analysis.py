listAll = []
while True:
    userInput = input()
    userInput = userInput.lower()
    theList = userInput.split()
    listAll.extend(theList)

    if listAll[len(listAll) - 1] == '###':
        frequent = 0
        for i in range(len(listAll)):
            a = 0
            for j in range(len(listAll)):
                if listAll[i] == listAll[j]:
                    a += 1
                ctr = a
            if frequent < ctr:
                frequent = ctr
                index = i
        print(listAll[index])
        break
