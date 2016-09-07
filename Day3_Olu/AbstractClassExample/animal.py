
class Animal(object):

    def __init__(self):

        #to make sure this abstract class is not instantiated, this is a place where i will raise an error
        raise NotImplementedError("You cannot instantiate an abstract class")

    def speak(self):

        #to make sure this abstract method is instantiated by the sub classes, this is a place where i will raise an error
        #instantiated here means overriding the method
        raise NotImplementedError("Please create a speak method for this abstract method")


