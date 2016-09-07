
class Animal(object):

    def __init__(self, name):
        self.__name = name

    def speak(self):

        print('I am an animal')
        print('My name is', self.__name)

    # here we change the default tostring mehtod
    # this is what is used when you print an object
    # which by default is to print the memory address
    def __str__(self):
        return 'I am an animal and my name is %s' % self.__name