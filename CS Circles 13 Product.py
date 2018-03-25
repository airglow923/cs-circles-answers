def prod(L):
    a = 1
    for i in range(0, len(L)):  # same as 'for i in L:' as L is the list
        a *= L[i]  # a = a * L[i]
    return a
