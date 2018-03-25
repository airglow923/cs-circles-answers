def mode(L):
    frequency = [0] * 10
    for i in L:
        frequency[i] += 1
    for i in range(0, 10):
        if frequency[i] == max(frequency):
            return i
