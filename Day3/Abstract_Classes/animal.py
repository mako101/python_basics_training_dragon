
class Animal(object):

    def __init__(self):

        # to make sure this abstract class is not instantiated,
        # this is where I will raise an error
        raise NotImplemented('You cannot instantiate an abstract class')

    def speak(self):

        # to make sure this abstract method is instantiated by the sub classes, I will raise an error here
        # instantiated here means overwritten
        raise NotImplemented('Please create a new speak method for your sub class')