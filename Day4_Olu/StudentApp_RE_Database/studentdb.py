import pypyodbc

class Student(object):

    __CONNSTR = "DRIVER={SQL Server}; SERVER=DESKTOP-RPGJTIP\SQLEXPRESS; DATABASE=Studentdb"

    def __init__(self, firstName, lastName, age, mobile, email):

        self.__firstName = firstName
        self.__lastName = lastName
        self.__age = age
        self.__mobile = mobile
        self.__email = email

    def saveStudent(self):

        #connect to the database
        conn = pypyodbc.connect(Student.__CONNSTR)

        #get a cursor to operate the database
        cur = conn.cursor()

        #run an sql command on the cursor
        cur.execute("Insert into Student(firstname, lastname, age, mobile, email) Values(?,?,?,?,?);",
                    (self.__firstName,self.__lastName, self.__age, self.__mobile, self.__email))

        #commit the change
        cur.commit()

        #close
        cur.close()
        conn.close()

    @staticmethod
    def getStudents():

        #connect to the database
        conn = pypyodbc.connect(Student.__CONNSTR)

        #get a cursor to operate the database
        cur = conn.cursor()

        #run an sql command on the cursor
        cur.execute("Select * from Student;")

        #display the column headers of your table
        for header in cur.description:
            print(header[0], end="    ")
        else:
            print()

        #print the content
        for row in cur.fetchall():

            for field in row:

                print(field, end="       ")
            else:
                print()

        #close
        cur.close()
        conn.close()
