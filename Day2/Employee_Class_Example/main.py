import employee

# create an instance od Employee class for 1st employee

emp1 = employee.Employee(1000)
emp1.name = 'Bob'

# because salary is hidden, we can not modify it, after the object has been created
# no error is given, just nothing happens
emp1.__salary = 1500
emp1.salary = 1500

# Same with ID
emp1.__id = 10


# create an instance od Employee class for 2nd employee

emp2 = employee.Employee(2000)
emp2.name = 'Mark'

#
# print('emp1 name is', emp1.name)
# print('emp2 name is', emp2.name)

print('emp1 display of name is')
emp1.display()

print('emp2 display of name is')
emp2.display()