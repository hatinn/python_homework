list = [0, 1, 245.0, 3.17, "2.50", "eight", False, "", True]
for x in list:
    if type(x) == int: print(x, ' is interger')
    if type(x) == float: print (x, ' is float')
    if type(x) != int: print(x, ' is NOT integer')
