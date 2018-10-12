def countup(n):
    if n == 0:
        print('Blastoff!')
        return None
    countup(n - 1)
    print(n)
