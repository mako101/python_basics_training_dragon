# what does the empoyee have: name, ID and salary
# what does the employee do: display

class Employee(object):

    # these are class variables
    # which means there is only once instance of them
    # if it is overwritten , it is changed everywhere
    name = "No Name" # not to be used
    empCount = 1    # we use this variable later!

    # constructor of the class
    def __init__(self, salary):

        # print a message to show that every time we create a new instance,
        # the constructor is being used
        print('Constructor called')

        self.employeeName = ''
        # this is a HIDDEN attribute. It CANNOT be modified in the instances of this class
        self.__id = Employee.empCount
        self.__salary = salary

        # increment the employee count every time we create a new employee!
        Employee.empCount += 1

    def display(self):

            print('Emplpoyee\'s ID is',  self.__id)
            print('Employee\'s name is', self.employeeName)
            print('Emplpoyee\'s salary is',  self.__salary)