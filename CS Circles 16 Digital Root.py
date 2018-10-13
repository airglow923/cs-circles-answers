def digitalRoot(n):
    if n < 10:
        return n
    else:
        n = digitalRoot(digitalSum(n))
        return n
