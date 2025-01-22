#match case is same as swithc case of language C
#Added in python 10+

# a = int(input("Enter 1 to 3, to see surprise"))
# match a:
#     case 1:
#         print("Entered number is 1")
#     case 2:
#         print("Entered number is 2")
#     case 3:
#         print("Exit Now")

#program to print table between 1 to 10

b = int(input("Enetr number between 1-5 to get table \n"))
match b:
    case 1:
        for i in range(10):
            print(1*(i+1))
    case 2:
        for i in range(10):
            print(2*(i+1))
    case 3:
        for i in range(10):
            print(3*(i+1))
    case 4:
        for i in range(10):
            print(4*(i+1))
    case 5:
        for i in range(10):
            print(5*(i+1))