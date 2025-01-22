class emp:
    def __init__(self, name, salary):       #constructor 
        self.name = name
        self.salary = salary
    # salary = 89
    # name = "rishi"
    def getSalary(self):
        print(self.salary)


# rohan = emp()

# print(rohan.getSalary())
# print(rohan.name)

ankit = emp("ankit", 100000)
# print(ankit.salary)
# print(ankit.name)
ankush = emp("ankush", 20000)
# print(ankush.name)
# print(ankush.salary)

ankit.getSalary()
ankush.getSalary()

