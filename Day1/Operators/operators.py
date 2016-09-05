# global variables

a = 50
b = 30

# create an arithmetic function
def arithmetic():

    # display
    print('This is an arithmetic operator')

    # # to set the local variables as global
    # # needs to be done BEFORE defining the variables
    # global a,b

    #local variables (overwrite global variables)
    a = 20
    b = 7

    # display a and b
    print('a is', a, 'and b is', b)

    # basic arithmetic operators
    print('a+b is:', (a + b))
    print('a-b is:', (a - b))
    print('a*b is:', (a * b))
    print('a/b is:', (a / b))
    print('a%b is:', (a % b))
    print('a**b is:', (a ** b))
    print('a//b (// means flooring) is:', (a // b))

    # Without a return, you are doing this:
    return None

def comparison():

    # display
    print('This is a comparison operator')

    # display a and b
    print('a is', a, 'and b is', b)

    # the comparison operators
    print('(a==b) is', (a == b))
    print('(a!=b) is', (a != b))
    print('(a>b) is', (a > b))
    print('(a<b) is', (a < b))
    print('(a>=b) is', (a >= b))
    print('(a<=b) is', (a <= b))


def assignment(x):

    # display
    print('This is an assignment operator')

    global b
    b = x

    print('Global b is', b)


    # b will NOT be modified with the operations below, just x

    # add a  to x
    x += a # same as x = x +a , no performance difference

    print('x is', x)

     # substract afrom x
    x -= a # same as x = x - a , no performance difference

    print('x is', x)

    # all other arithmetic operators can be used in the same way
    x *=a ; print('x is', x)
    x /=a ; print('x is', x)
    x %=a ; print('x is', x)
    x **=a ; print('x is', x)
    x //=a ; print('x is', x)


def logical(a,b):

    # display
    print('This is a logical operator')

    # display a and b
    print('a is', a, 'and b is', b)

    # the logical operators
    print('(a and b) is', (a and b))
    print('(a or b) is', (a or b)) # true if either is true or both
    print('(a xor b) is', (a ^ b)) # true if either is true but NOT both
    print('not (a and b) is', not (a and b))
    print('not (a or b) is', not (a or b))



def membership():

    global a,b

    a = 50
    b = 50 # '50'

    # display a and b
    print('a is', a, 'and b is', b)

    # membership uses keywords 'is' and 'is not'
    # it compares values AND datatypes
    # both must be equal for comparison to be true

    print('a == b):', (a == b))
    print('a is b):', (a is b))
    print('a is not b):', (a is not b))

    # as is NOT the same as class int
    print('a is int):', (a is int))
    print('a is not int):', (a is not int))

    print()
    a = '50'
    b = str(50)

    # display a and b
    print('a is a string:', a, 'and b is result of a function:', b)

    print('a == b):', (a == b))

    print('a is b):', (a is b))
    print('a is not b):', (a is not b))

def identity(word, sentence):

    # display
    print('This is an identity operator')

    # display word and sentence
    print('Word is:', word, '||', 'Sentence is:', sentence)

    # identity is used with keywords 'in' and 'not in'
    print('word in sentence:', (word in sentence))
    print('word not in sentence:', (word not in sentence))