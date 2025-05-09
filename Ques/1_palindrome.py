# value is same from the end, exam : madam, 12321,
# x = [] #list
# y = {"madam"}  #Set
# z = ()  #tuple
# a = {'a':10, 'b':20}    #dictionary

string = "45654"
sum = 0
l = (len(string))
end = (l-1)
for x in range (int(l/2)):
    if(string[x] == string[end-x]):
        sum = sum+1
    else:
        print("Not a palindrome")
        exit()

if(sum > 1):
     print("Value is palindrome")