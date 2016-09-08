import re
import studentdb

def saveStudent():

    # ask user details
    firstname = input('What is the student\'s first name?')
    lastname = input('What is the student\'s last name?')
    age = input('What is the student\'s age?')
    mobile = input('What is the student\'s mobile?')
    email = input('What is the student\'s email?')

    # validate mobile
    # we dont check in if the user doesnt eneter anythin as this is an optional fielsd
    if mobile != '':
        pattern=r"\d{11}"

        mobileMatch = re.match(pattern, '')

        if not mobileMatch:
            print('Please enter a valid number of 11 characters')

        #repeat
        print()
        saveStudent()

    #validate age
    if age != '' and not str(age).isdigit():
        print('Age must be valid')



    #create an instance of the student class
    stud = studentdb.Student(firstname, lastname, age, mobile, email)

    try:
        stud.saveStudent()

        print('Student Saved Successfully')

    except Exception as e:
        print('Student was NOT saved')
        print(e)


    # display all sudents
    print('*' * 30, 'STUDENT RECORDS', '*' * 30)
    studentdb.Student.getStudents()

     # repeat
    saveStudent()

#####################START########################

saveStudent()