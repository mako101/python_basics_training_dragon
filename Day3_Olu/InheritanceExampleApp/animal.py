
class Animal(object):

    def __init__(self, name):

        self.__name = name

    def speak(self):

        print("I am an animal")
        print("My name is", self.__name)

    def __str__(self):

        return "This animal is named " + self.__name