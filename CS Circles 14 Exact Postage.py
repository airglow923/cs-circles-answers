def postalValidate(S):
   S = S.replace(' ', '')
   if S.isalpha() or S.isdigit() == True:
      return False
   else:
      if len(S) == 6:
         if (S[0].isalpha() and S[2].isalpha() and S[4].isalpha()) == False:
            return False
         else:
            if (S[1].isdigit() and S[3].isdigit() and S[5].isdigit()) == False:
               return False
            else:
               return S.upper()
      else:
         return False

import re # This working is coded by a user from StackOverFlow

def postalValidate(S):
    S = S.replace(' ', '')
    pattern = re.compile('^([a-zA-Z][0-9]){3}$')

    if pattern.match(S):
        return S.upper()
    else:
        return False
