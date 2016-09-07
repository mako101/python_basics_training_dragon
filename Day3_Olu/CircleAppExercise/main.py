#create an application that displays the area and circumference of a circle continously
#the application should store a pi variable as 3.14
#the application should ask user for the radius
#for example, if user types 4 for radius
#application should display
#area = 3.14 * 4 * 4
#circumference = 2 * 3.14 * 4

#handle exception where necessary
#use classes where necessary

import circle

#create an instance of the circle class
cir = circle.Circle()

def startApp():

    #radius variable
    radius = 0

    try:

        #ask the user for the radius
        radius = float(input("What is the radius of your circle?"))

    except ValueError:
        print("radius must be a number e.g. 5.6")

    except:
        print("An error occured, please contact IT Support")

    #display the area and circumference
    print("The area of the circle is %scm^2" %cir.getArea(radius))
    print("The circumference of the circle is %scm" %cir.getCircumference(radius))

    #call the tostring method of the object
    print(cir)

    #continue via recursion
    print()
    startApp()


#call the startapp method
startApp()