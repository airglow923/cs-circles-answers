def replace(list, X, Y):
   while list.count(X) > 0: # equals to 'while X in list:'
      a = list.index(X)
      list.pop(a)
      list.insert(a, Y)
