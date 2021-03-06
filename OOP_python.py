"""
    Object-oriented programming in Python is very simple and easy to understand.
    In the following example we will try declaring a class named Employee to explain how
    OOP works in Pyhton.
"""

class Employee(object):
    numEmployee = 0
    def __init__(self,name, rate):
        self.owed = 0
        self.name = 0
        self.rate = rate
        Employee.numEmployee += 1

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self,numHours):
        self.owed += numHours*self.rate
        return ("%.2f hours worked" %numHours)

    def pay(self):
        self.owed = 0
        return ("payed %s"%self.name)