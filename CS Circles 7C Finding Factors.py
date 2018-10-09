n = int(input())
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a * b == n:
            print (a, 'times', b, 'equals', n)
