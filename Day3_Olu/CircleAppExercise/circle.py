
class Circle(object):

    #pi is 3.14
    __PI = 3.14

    def __init__(self, radius = -1):

        #Polymorphism here
        self.__radius = radius #radius of the circle

    def getArea(self, radius = -1):

        if radius != -1:
            self.__radius = radius

        area = self.__PI * self.__radius * self.__radius

        #return area to 2 decimal places
        return round(area, 2)


    def getCircumference(self, radius = -1):

        if radius != -1:
            self.__radius = radius

        circumference = 2 * self.__PI * self.__radius

        #return circumference to 2 decimal places
        return round(circumference, 2)


    #destructor
    def __del__(self):
        print("Circle object is destroyed")


    # #override the tostring method
    def __str__(self):

        return "This is a circle with radius of %s cm" %(self.__radius)