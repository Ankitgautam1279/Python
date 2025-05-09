import time
t = time.localtime(time.time())

print("Current time is", end=" :: ")
print(time.strftime("%H : %M : %S", t))
# hrs = int(time.strftime("%H"))
# min = time.strftime("%M")
# sec = time.strftime("%S")

# if(hrs < 12 and hrs > 00):
#     print("Good Morning")
# elif(hrs < 18 and hrs > 12):
#     print("Good Evening")
# else:
#     print("Good Night")


        # 2nd method

import datetime

x = datetime.datetime.now()
y = datetime.datetime(2012,2,12)
# print(x)
# print(y)

# yrs = x.strftime("%Y")
# print(yrs)
# hrs = x.strftime("%H")
# print(hrs)
