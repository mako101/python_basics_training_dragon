# create a functon that adds 2 numbers together:

# normal function:

def addNumbers(a,b):
     return a + b


# hidden function
def addNumbersHidden(a,b):
    def add(x,y):
        return x + y

    # now we call the result of internral function
    return(add(a,b))

print(("*")* 50)

a = 50
b = 20

# display

print("a is %s and b is %s" % (a,b))

# call normal function
print('Addition with addNumbers is', addNumbers(a,b))
print('Addition with addNumbersHidden is', addNumbersHidden(a,b))

# cannot call the addNumbersHidden.add(a,b) fucntion!
#addNumbersHidden.add(a,b)

# lambda
addNumbersLambda = lambda a,b: a + b
print('Addition with addNumbersLambda is', addNumbersLambda(a,b))
print(type(addNumbersLambda))
