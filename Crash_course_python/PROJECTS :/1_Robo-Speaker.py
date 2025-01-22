import os
if __name__ == '__main__':
    print("Welcome in robo speaker, Press q to exit ")
    while True:
        x = input("What you want to speak : ")
        if(x == "q"):
            os.system("say 'Bye Bye, thank you for using' ")
            break
        command = f"say {x}"
        print(command)
        os.system(command)

    