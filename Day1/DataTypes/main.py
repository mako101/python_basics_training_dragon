# variable with the integer value
num1 = 56
# display the type of num1
print('The type of num1 is', type(num1))


# variable with float value
num2 = 5.8
# display the type of num2
print('The type of num2 is', type(num2))

# variable type Boolean
num3 = False
# display the type of num3
print('The type of num3 is', type(num3))

num4 = -0x1243
# display the type of num4 - converts hex to integer
print('The type of num4 is', type(num4))

# string variables

mystring1 = 'This is a sigle quote string'
# mystring1 = 'This is a sigle quote string
#             mystring1 cannot be on mutliline'

mystring2 = "This is a double quote string"
# mystring2 = "This is a double quote string
#             mystring2 cannot be multi line"

mystring3 = '''This is a triple single quote string
            and it can be multi line'''

mystring4 = """This is a triple double quote string
            and it can be multi line"""

mystring5 = 'This is a single quote string' \
    'and it is split, but this is not recommended!'

# del is used to delete objects from memory
# del mystring1

print('mystring1:', mystring1); print('mystring2:', mystring2)#this works but should not be used!
print('mystring3:', mystring3)
print('mystring4:', mystring4)
print('mystring5:', mystring5)

# slicing
print('The first character of mystring1:', mystring1[0]) # referred by index
print('The third character of mystring1:', mystring1[2]) # referred by index
print('The fourth character of mystring1 to the end of sentence:', mystring1[3:]) # referred by index
print('The fourth character of mystring1 to the 11th character:', mystring1[3:11]) # referred by index AND position!
print('The second character of mystring1 from the end:', mystring1[-2]) # referred by position
print('The second character of mystring1 from the end and to the end of the string:', mystring1[-2:]) # referred by position
# print('The 1000th character of mystring1:', mystring1[999]) # this will break, as index is out of range
