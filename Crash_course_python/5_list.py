l1 = [12,4,90,6,8]
# print(l1)
# print(type(l1))
# print(l1[3])
# l1.remove(6)
# print(l1)         //modify same list & keep updating bcoz list is mutable
# l1.sort()
l1.pop(2) #90 will be removed, from index 2
l1.extend([17,21,23,35])
print(l1)
# l1.clear()
print(l1.index(17)) #return the index of 17 from list
print(l1) 
l1.append(29)
print(l1)
