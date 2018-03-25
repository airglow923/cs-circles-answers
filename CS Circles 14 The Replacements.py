def replace(list, X, Y):  # 'list' equals to the list of numbers
   while list.count(X) > 0:  # same as 'while X in list:'
      a = list.index(X)  # locate where the 'X' value is in the list 
      list.pop(a)  # remove the 'x' value
      list.insert(a, Y)  # insert (or replace) the 'X' value into the 'Y' value
