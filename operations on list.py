
list1=[10,20,30,40,50,100]
print(len(list1))
str='aeiou'
list2=list(str)
print(list2)

print(min(list1))
print(max(list1))
print(sum(list1))
list1.append(60)
print(list1)
list1.append(70)
print(list1)

print(type(list1))

list1.extend([90,100,200])
print(list1)
list1.insert(2,25)
print(list1)

print(list1.count(100))
print(list1.index(100))
list1.remove(90)
list1.pop(0)
print(list1)
list1.reverse()
print(list1)
list1.sort(reverse=True)
print(list1)
