# import custom functions for statistics and file operations
import stats_file_ops as s

import sys

# We need a list to collect numbers into
numbers = []


# logic to process the user's input
def process_input(user_input):

    # if a number is passed, we add it to the array
    if type(user_input) == int:
        numbers.append(user_input)
        print('Number added to the list!', '\n')

    # parsing string data
    elif type(user_input) == str:

        # Calculating statistics
        if user_input == 's':

            # Make sure at least one number has been given
            if len(numbers) >= 1:

                s.calculate_statistics(numbers)
                sys.exit()

            else:
                # Complain and exit
                print('Please pass some numbers first!')
                sys.exit()

        # saving data to a file
        elif user_input == 'w':

            # we will write the list to a file
            s.write_to_file(numbers)
            print()

            # now we will read the file
            s.read_file()
            sys.exit()

        # terminate program
        elif user_input == 'q':

            print('Goodbye!')
            sys.exit()

        else:
            print('Invalid option given')

    # reject all other data types
    else:
        print('Invalid option given')