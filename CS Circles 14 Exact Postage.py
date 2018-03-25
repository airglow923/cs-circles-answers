def postalValidate(S):
    S = S.replace(' ', '')  # remove all the spaces
    
    if S.isalpha() or S.isdigit() == True:  # if the input is comprised of only letters or digits
        return False
    else:
        if len(S) == 6:  # the input should not be more or less than 6 characters
            if (S[0].isalpha() and S[2].isalpha() and S[4].isalpha()) == False:  # if there is any letter in the position of digits
                return False
            elif (S[1].isdigit() and S[3].isdigit() and S[5].isdigit()) == False:  # if there is any digit in the position of letters
                return False
            else:  # if letters and digits are all in the right places
                return S.upper()  # convert all the letters into capital letters
        else:  # if the input is more or less than 6 characters
            return False

        
# another method uses regex        
import re

def postalValidate(S):
    S = S.replace(' ', '')  # remove all the spaces
    
    pattern = re.compile(r'([a-zA-Z][0-9]){3}$')  # 'L#L#L#', 'L' ranging from a to z and A to Z, '#' ranging from 0 to 9, {3} means to repeat 'L#' pattern 3 times

    if pattern.match(S):  # if the input fits into the format of 'L#L#L#'
        return S.upper()  # conver all the letters into capital letters
    else:  # if the input does not fit into the format of 'L#L#L#'
        return False
