needle = input()  # define the first input string
haystack = input()  # define the second input string
times = 0  # define how many times the needles will be counted
for a in range(0, len(haystack) - 1):  # loop to check strings within haystack
    if haystack[a:len(needle) + a] == needle:  # check for needles in haystack
        times += 1  # count the number of needles
print(times)
