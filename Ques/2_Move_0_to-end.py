
a = [2,3,0,3,5,6,34,0,56,78,89,0,12,234]
# print(a, "\n")
# l = len(a)
# ind = a.index(0)

# for i in range (ind,l-1):
#     a[i] = a[i+1]
    
# a[l-1] = 0
# print(a)

    # OR 

for x in (a):
    if x ==0:
        a.remove(0) 
        a.append(0)

print(a)