import animal

class Dog(animal.Animal):

    def __init__(self, name):

        self.__name = name

    def speak(self):

        print("This is a dog named,", self.__name)