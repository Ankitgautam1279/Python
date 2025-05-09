class Democlass:
    a = 10
    def __init__(self): 
        print("Hello : This is Constructor")

    def showvalue(self,b,c):
        print(self.a)
        print(" function called :",b+c)

# demo = Democlass() 
# to create object
# print(demo.a)
# demo.showvalue(15,17)
# demo.showvalue(10,20)

class A:
    def displayA(self):
        print("Class A display func called")

class B(A):
    def displayB(self):
         print("Class B display func called")

class C(B,A):   
    def displayC(self):
        print("Class C called")

inher = B()
# inher.displayA()
# inher.displayB()
multi = C()
# multi.displayA()
# multi.displayB()
# multi.displayC()


class getter:
    def __init__(self):
        self.__name = ""
        print("Acessing private attribute using name Mangling")

    def getname(self):
        return self.__name
    
    def setname(self,name):
        self.__name = name

g = getter()
print(g._getter__name)
# Private attribute renamed as [_classname__attribute name] , & can be accessed in this way but not directly
g.setname("setter function in Python")
print(g.getname())