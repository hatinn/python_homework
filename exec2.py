list = [0, 1, 245.0, 3.17, "2.50", "eight", False, "", True]
a = 0.0
for x in list:
    if type(x) == int: 
        float(x) 
        a += x
    if type(x) == float: 
        a += x
print(a)
