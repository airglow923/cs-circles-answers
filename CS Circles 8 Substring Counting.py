needle = input()   #defines first input string
haystack = input()   #defines second input string
times = 0   #defines number of times first input string is in second
for a in range(0, len(haystack) - 1):   #loop to check strings within haystack
    if haystack[a:len(needle) + a] == needle:   #checking for needle in haystack
        times = times + 1   #increasing our number of occurances if true
print(times)   #and here is your output
