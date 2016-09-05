# need to split logic better
# each element should be reusable!
# main should put everything together
# e.g the logic module should't care how the variables are passed, only how to process them!
# main module will deal with gathering data
# see Olu's examples

from arenaLogic import main_logic


def start_app():

    # Lets get all the data from the user
    name = input('What is your name?: ')
    age = input('What is your age?(numbers only): ')
    gender = input('What is your gender?(type M or F:) ')

    # Let's catch some exceptions
    try:
        main_logic(name=name, age=age, gender=gender)

    # This is a possible error we know about, so we can tell the user how to avoid it
    except ValueError:
        print('Please enter age as a number')

    # This is a generic message for the errors we dont expect!  A developer needs to look at these
    except:
        print('Something went wrong, please contact IT Support!')


start_app()
