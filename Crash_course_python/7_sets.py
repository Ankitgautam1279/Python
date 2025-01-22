set = {12,23,6,6,6,34,45,45,6} #set start with {} & No duplicacy allowed
set2 = {1,2,3,4,5,6,5}
print(type(set))
print(set)
set.pop()   #remove any one value from set
print(set)
print(set.union(set2))
print(set.intersection(set2))
