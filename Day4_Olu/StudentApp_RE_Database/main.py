import re
import studentdb

def saveStudent():

    #ask
    firstname = input("What is the student's first name?")
    lastname = input("What is the student's last name?")
    age = input("What is the student's age?")
    mobile = input("What is the student's mobile?")
    email = input("What is the student's email?")

    #validate mobile
    if mobile != "":
        pattern = r"\d{11}"

        mobileMatch = re.match(pattern, mobile)

        if not mobileMatch:
            print("Please enter a valid mobile phone number of 11 characters e.g. 070asdfLKJH")

            #repeat
            print()
            saveStudent()

    #validate age
    if age != "" and not str(age).isdigit():
        print("Age must be a number e.g. 22")

        #repeat
        print()
        saveStudent()

    #create an instance of student class
    stud = studentdb.Student(firstname, lastname, age, mobile, email)

    try:

        #save the student
        stud.saveStudent()

        print("Student Saved Successfully")

    except Exception as e:
        print("Student not saved successfully", e)

    #display all students
    print("*" * 30, "STUDENT RECORDS", "*" * 30)
    studentdb.Student.getStudents()

    #repeat
    print()
    saveStudent()

####################start#######################

#display all students
print("*" * 30, "STUDENT RECORDS", "*" * 30)
studentdb.Student.getStudents()

#save student
saveStudent()