

def main_logic(name, age, gender):

    # Make sure age is an integer
    age = int(age)

    # Make sure gender is string and in capitals
    gender = str.upper(gender)

################ Hidden function!! ########################
    # if you define function inside a function, it cannot be called as a method
    # Figure our the title for the user
    def getTitle(age, gender):
        if age < 18 and gender == 'M':
            title = 'Master'
        elif age < 18 and gender == 'F':
            title = 'Miss'
        if age > 18 and gender == 'M':
            title = 'Mr'
        elif age > 18 and gender == 'F':
            title = 'Ms'
        return title
#############################################################

    title = getTitle(age, gender)

    def allowAccess(title, name):
         print('Hello %s %s, you are allowed in this area' % (title, name))

    if age < 18:
        # no under 18's allowed
        print('Hello %s %s, you are not allowed in this area' % (title, name))

    elif age > 18:

        # Girls go free
        if gender == 'F':
            allowAccess(title, name)

        elif gender == 'M':
            # guys between 18 and 50 must pay
            # if 18 < age > 50:
            if (age >= 18) and (age <= 50):
                payment = str.upper(input('Do you wish to pay?(type Y for Yes or N for No): '))
                if payment == 'Y':
                    allowAccess(title, name)
                elif payment == 'N':
                    print('Thank you %s %s, goodbye!' % (title, name))

            else:
                allowAccess(title, name)

        else:
            print("invalid gender supplied")


