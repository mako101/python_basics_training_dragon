class Rectangle(object):

    def __init__(self, length, width):

        # Calculate perimeter and width from given arguments
        self.perimeter = (length + width) * 2
        self.area = length * width

    def display_perimeter(self):
        print('The perimeter is', self.perimeter)

    def display_area(self):
        print('The area is', self.area)
