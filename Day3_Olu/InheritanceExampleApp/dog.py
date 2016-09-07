import animal

class Dog(animal.Animal):

    def __init__(self, name, leg):

        #call the super class constructor
        super().__init__(name)

        self.__leg = leg

    #second polymorphism - method override
    #override the method of the super class
    def speak(self):

        #call the superclass method
        super().speak()

        print("I am a dog")