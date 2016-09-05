# import maths for statistical operations
import statistics as s


# function to calculate all statistics
def calculate_statistics(numbers):

    try:

        print('You have supplied the following numbers:')

        for number in numbers:
            # print all numbers on one line
            print(number, end=' ')

        print('\n')

        print('The statistics for your numbers are:\n')

        mean = s.mean(numbers)
        print('%.2f' % mean)  # rounded up

        median = s.median(numbers)
        print('Median:', median)

        mode = s.mode(numbers)
        print('Mode:', mode)

    # if there 2 or more numbers that are equally frequent, mode function will crash
    except s.StatisticsError:
        print('Mode cannot be calculated for this data set')

# function to write to a file
def write_to_file(numbers):
    file = open('numbers.txt', 'w')

    # convert numbers to string, so that we can write it to file
    file.write(str(numbers))
    file.close()
    print('The numbers have been written to a file')

# function to read from a file
def read_file():
    file = open('numbers.txt', 'r').read()
    print('The contents of the file are:')
    print(file)