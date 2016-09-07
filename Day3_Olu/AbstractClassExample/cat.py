import animal

class Cat(animal.Animal):

    def __init__(self, name):

        self.__name = name

    def speak(self):

        print("This is a cat named,", self.__name)