somestring = input('Enter the string you wish: ')
alist = somestring.split("; ")
blist = list()
d = dict()
f = 0

for x in alist:
    blist = blist + x.split(" = ")
for x in range(0, len(blist)-1, 2):
    a = blist[x]
    x = x+1
    b = blist[x]
    d[a] = b
print("initial dictionary", d)

d_inv = {x: y for y, x in d.items()}
print("inverted dictionary", d_inv)

for key, value in sorted(d.items()):
    print("{} : {}".format(key, value))
    f += 1
    if f < int(len(blist)/2):
        for x in range(50): print("#", end='')
        print()
