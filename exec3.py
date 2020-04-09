somestring = input('Enter the string you wish: ')
alist = somestring.split(" ")
print(alist[0])
print(alist[-1])
aset = set(alist)
a = 0
for x in aset:
    a += 1

print (a)
