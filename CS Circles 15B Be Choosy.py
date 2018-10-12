def choose(n, k):
    foo = 1
    for i in range(n):
        foo *= n - i

    bar = 1
    for i in range(k):
        bar *= k - i

    baz = 1
    for i in range(n - k):
        baz *= (n - k) - i

    return foo/(bar*baz)

# For more information: https://en.wikipedia.org/wiki/Combination
