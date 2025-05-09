x = int(input('''Enter 1 for Add
          Enter 2 for Substract
          Enter 3 for Multiplication
          Enter 4 for division >> 
          '''))
match x:
    case 1:
        print("Number will be added here")
    case 2:
        print("Number will be Substracted here")
    case 3:
        print("Number will be Multiplied here")
    case 4:
        print("Number will be Divided here")
