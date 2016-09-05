
# grading function
def getGrade(grd):
    result = 'Invalid grade supplied'

    # convert to uppercase
    grd = str.upper(grd)

    if grd == 'A':

        result = 'Excellent Grade'

    elif grd == 'B':

        result = 'Good Grade'

    elif grd == 'C':

        result = 'Fair Grade'

    elif grd == 'D':

        result = 'OK Grade'

    elif grd == 'E':

        result = 'Pass Grade'

    elif grd == 'F':

        result = 'Failed Grade'

    return result