try:
    a = int(input("Enter your number : "))
    print(a + 3)
except:
    print("some error occured")

        #we can also provide exception details
try:
    a = int(input("Enter your number : "))
    print(a + 3)
except Exception as e:
    print("some error occured", e)
