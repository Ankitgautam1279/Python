l = []

for a in range(11,1,-1):
    l.append(a)

print(l)


m = [x+2 for x in range(1,11) if x%2 ==0]

print(m)

# List comprehensive is short form, in which multiple expressions + condition can be written