def digitalSum(n):
    if n < 10:
        return n
    else:
        i = digitalSum(n // 10)
        n %= 10
        i += n
        return i
