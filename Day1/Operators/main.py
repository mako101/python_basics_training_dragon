import operators as op

# call the arithmetic function
op.arithmetic()

# line space
print()

# call the comparison function
op.comparison()

# line space
print()


# call the assignment function
op.assignment(45)

# line space
print()

# call the logical function
op.logical(True, True) # positional arguments
# This is assigned by position. It means a is True and b is False
#  What if you wanted to say a is False and b is True, using the same position?

# line space
print()

# the solution is using Named Arguments
op.logical(b=True, a=False)

# line space
print()

# call the membership function
op.membership()

# line space
print()

# call the identity function
op.identity('hello', 'this is the hello world')