import rectangle as r

def startApp():

    width = 0
    length = 0

    try:
        width = float(input('Please specify the width: '))
        length = float(input('Please specify the length: '))
    except ValueError:
        print('Please type digits only')

        return startApp()

    rec = r.Rectangle(width,length)

    rec.display_area()
    rec.display_perimeter()
    print()

    startApp()

startApp()