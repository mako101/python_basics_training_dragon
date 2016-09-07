# Create an application that displays the area and circumference of the circle continuously
# the application should store the pi variable as 3.14
# the application should ask user for the radius
# for example if radius of 4 is given:
# application should display
# area = 3.14 * 4 * 4
# circumference = 2 * 3.14 * 4


import circle as c

circ =  c.Circle()



def startApp():


    radius = 0

    try:
        radius = float(input('Please specify the radius: '))
    except ValueError:
        print('Please type digits only')

        return startApp()

    # general exception
    except:
        print('Somthing went wrtong, please contact IT Support')

    print('The area of the circle is', circ.getArea())
    print('The circumference of the circle is', circ.getCircumference())

    startApp()

startApp()