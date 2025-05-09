import array as arr

list1 = []
# print(type(list1))
list1 = [22,44,33]
list2 = ["pryag", "ayodhya", "kumbh"]
list3 = [4.5, "abc", True]
list1.sort()        #list1 sorted

# print(list1, "\n", list2, "\n", list3)
# for e in list2:
#     print(e)
# print(sum(list1))
# print(max(list1))
# print(min(list1))
# list2.insert(2, "pundar")  #  TO INSERT DATA, WE PROVIDE (INDEX NUMBER , VALUES)
# print(list2)

a = arr.array('i', [12,15,13,16]) #we can provide 2 arguement only, 1st ; dataType & 2 : list
# print(a)
# for e in a:
#     print(e)
# print(a[-1])    #minus index stats from end
# print(*a)   #print array without datatype, seperated by space
# a.append(30)
# a.pop(1) #provide index to pop, by default last value
# a.insert(4,5)
# a.append(23)
# print(a)
# print(a[1:5])
# print(a[::-1])
print(a.index(13))
a.extend([1,2,3,4])
print(a)

# signed char / unsigned char : 1 bytes
# signed short/ unsigned short : 2 bytes
# signed int / unsigned int : 2 bytes
# signed long / unsigned long : 4 bytes
# signed & unsigned Long long : 8 bytes
# float : 4 bytes
# double : 8 bytes