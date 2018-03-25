def isPalindrome(S):
    if str(S) == str(S)[::-1]:  # if 'S' equals to the inverse of 'S'
        return True
    else:
        return False
