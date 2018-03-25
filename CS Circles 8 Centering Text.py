width = int(input())  # the length of text
while True:
    a = input()  # word for centering
    L = len(a)  # length of the word
    b = (width-L) // 2  # calculate how many periods are needed on both sides of the word (left side)
    c = b  # this will be used for unbalanced length (right side)
    
    if ((width-L) % 2) != 0:  # if periods needed on both sides are unequal
        b = b + 1  # add one more period on the left side
    if a == 'END':  # if the input is 'END'
        break
        
    print('.' * b + a + '.' * c)
