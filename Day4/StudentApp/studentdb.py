import pypyodbc

class Student(object):

    _CONNSTR = 'DRIVER={SQL SERVER};  SERVER=DESKTOP-RPGJTIP\SQLEXPRESS; DATABASE=StudentDB'

    def __init__(self, firstName, lastName, age, mobile, email):

        self.__firstname = firstName
        self.__lastname = lastName
        self.__age = age
        self.__mobile = mobile
        self.__email = email


    def saveStudent(self):
        # connect to database
        conn = pypyodbc.connect(Student._CONNSTR)

        # get a cursor to opeate the database
        cur = conn.cursor()

        # run an SQL command on the cursor
        cur.execute('Insert into Student(firstname, lastname, age, phone, email) Values(?,?,?,?,?);',  (self.__firstname, self.__lastname, self.__age, self.__mobile, self.__email))

        # commit - need to do this when applying db changes
        cur.commit()

        #close connections
        cur.close()
        conn.close()

    @staticmethod
    def getStudents():

        # connect to database
        conn = pypyodbc.connect(Student._CONNSTR)

        # get a cursor to opeate the database
        cur = conn.cursor()

        # run an SQL command on the cursor
        cur.execute('Select * from Student;')

        # display the column headers from your table
        for header in cur.description:
            print(header[0], end='      ')

        else:
            print()

        #print the content
        for row in cur.fetchall():
            for field in row:
                print(field, end='            ')
            else:
                print()

        #close connections
        cur.close()
        conn.close()