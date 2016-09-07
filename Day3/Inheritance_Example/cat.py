import animal

class Cat(animal.Animal):

    # we want to specify the race of a cat
    def __init__(self, name, race):

        #
        super().__init__(name)

        self.__race = race

    def speak(self):
        print('I am a %s cat' % self.__race)

        # import the supercalss speak function
        super().speak()

