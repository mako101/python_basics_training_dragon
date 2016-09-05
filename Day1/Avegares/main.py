# logic for processing the user input
from process_input import process_input
import re


def start_app():

    # Tell the user how to use the program and get their input:
    user_input = input('''Please give one of the following options:
    Any number - to be added to your list of numbers
    s - to calculate statistics on your numbers
    w - to write the list of numbers to a file
    q - to exit the program\n
    ''')

    # if there are numbers (and only numbers) in the user's input,
    # we need to convert it to integer
    if re.match("[0-9]+", user_input):
        try:
            user_input = int(user_input)
        except ValueError:
            print('Please give either a number or a letter\n')
    else:
        # convert string to lowercase
        user_input = user_input.lower()

    # process the user's response
    process_input(user_input)

    # run again
    start_app()


start_app()
