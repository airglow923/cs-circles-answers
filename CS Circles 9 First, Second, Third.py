a = int(input())  # convert input into integer as it is always a string
if a / 1 == 1:  # if the input can be divided by 1
    print(str(a) + 'st')  # 1st
elif a / 2 == 1:  # if the input can be divided by 2
    print(str(a) + 'nd')  # 2nd
elif a / 3 == 1:  # if the input can be divided by 3
    print(str(a) + 'rd')  # 3rd
else:  # if not 1st, 2nd and 3rd
    print(str(a) + 'th')  # (number)th
