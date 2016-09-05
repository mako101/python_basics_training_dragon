import grade


# grd = input('What is your grade?: ')
#
# # display grade
#
# print(grade.getGrade(grd))

# calling the function repeatedly
def startApp():

    #ask for grade
    grd = input('What is your grade?: ')

    # display grade result
    print(grade.getGrade(grd))

    # empty line
    print()

    # recursion to repeat - careful to avoid infinite loops!
    startApp()

startApp()

# For the best perfomance (ie using the least memory), we should pass argument to startApp, like this
# startApp(grd)
# This way it will reuse the grd variable in memory during each execution,
#  rather then create new grdvariable everytime and store it in memory, like in the example above