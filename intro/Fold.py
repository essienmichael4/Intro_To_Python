from functools import reduce

#Fold Example
total = print(list(reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])))
