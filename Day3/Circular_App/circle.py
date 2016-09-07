
class Circle(object):

    # this is a class variable, that will be used in methods
    pi = 3.14

    def __init__(self, radius = 1):
        self.__radius = radius


    def getArea(self, radius = -1):

        # polimorfism here
        # if we have passed the radius value, it will use the user defined one
        # if we dont, it will usen the default __radius value
        # the app will run either way!

        # using default value
        if radius == -1:
             return self.pi * self.__radius ** 2

        else:
            return self.pi * radius ** 2

    # same here
    def getCircumference(self, radius = -1):

        if radius == -1:
             return 2 * Circle.pi * self.__radius

        else:
            return 2 * Circle.pi * radius