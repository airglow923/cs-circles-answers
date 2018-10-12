letterGoodness = [0.0817, 0.0149, 0.0278, 0.0425, 0.127,
                  0.0223, 0.0202, 0.0609, 0.0697, 0.0015,
                  0.0077, 0.0402, 0.0241, 0.0675, 0.0751,
                  0.0193, 0.0009, 0.0599, 0.0633, 0.0906,
                  0.0276, 0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

userInput = input()
userInput = list(userInput)

highest = 0
total = 0
for S in range(0, 27):
    total = 0
    for i in range(len(userInput)):
        if userInput[i] == ' ':
            continue
        letterNum = ord(userInput[i]) - S

        if letterNum in range(65, 91):
            total += letterGoodness[letterNum - 65]
        else:
            letterNum = -(letterNum - 65) - 1
            total += letterGoodness[letterNum]

    if highest < total:
        highest = total
        index = S

result = ''
for i in range(len(userInput)):
    if userInput[i] == ' ':
        result += userInput[i]
    elif ord(userInput[i]) - index not in range(65, 91):
        result += chr(ord(userInput[i]) - index + 26)
    else:
        result += chr(ord(userInput[i]) - index)

print(result)
