import animal

class Dog(animal.Animal):
    '''to do'''

    def __init__(self, name, leg):

        # call the super class constructor
        super().__init__(name)

        # the attributes should be hidden unless you specifically want the user to see them
        self.__leg = leg

    # second polymorphism - mehtod overwrite
    # overwrte method of the superclass
    def speak(self):
        print('I am a dog!')

        # you can still call the method from the superclass
        super().speak()