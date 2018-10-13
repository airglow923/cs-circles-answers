def hailstone(n):
    print(n)
    if n == 1:
        return None
    elif n % 2 == 0:
        return hailstone(int(n / 2))
    else:
        return hailstone(int(3*n+1))
