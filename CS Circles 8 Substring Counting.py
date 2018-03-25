needle = input()   # defines first input string
haystack = input()   # defines second input string
times = 0   # defines number of times first input string is in second
for a in range(0, len(haystack) - 1):   # loop to check strings within haystack
    if haystack[a:len(needle) + a] == needle:   # checking for needles in haystack
        times += 1   # counting the number of needeles
print(times)
