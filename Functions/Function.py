# Function -- Returns a Value (None or Real) based on the given argument.
# Arguments -- Fixed Length & Variable Length
    # Variable function arguments or Non-Keyword Arguments
    # Python Default arguments
    # Python Keyword arguments

# Python Arbitrary arguments

#Non-Keyword Arguments
def sample(a,b):
    result = a+b
    return result

sample(3,5)

# Default Arguments
def sample(a,b=4):
    result = a+b
    return result

# print(sample(3,b=8))  # Non-Default and default should come second

# Keyword Arguments with positional combination
def sample(a,b):
    result = a+b
    return result

#print(sample(a=3,b=8))
#print(sample(b=8,a=3))
#print(sample(6, b=1))  # Positional or Non-Keyword Argument should be called first followed by Keyword Argument

# Python Arbitrary arguments
# *args or *<variable_name>
# Whenever I don't know the length of the argument
# Always works with Non-Keyword Arguments
def summation1(*args):
    '''docstring: Description -- This function add all the arguments'''
    sum = 0
    for i in args:
        sum = i + sum
    return sum

t = [1,2,3,5,6,7,8,12,32]   # Variable Can be Tuple or List
#print(summation(*t))

# Python Keyword Arbitary Arguments
# Always works with Keyword Arguments
# **kwargs or *<variable_name>
# Whenever I don't know the length of the argument
def Depack(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
key_arg = {'a':'1','b':'2'} #,c='3',d='4}
# Depack(**key_arg)

# When we pass Keyword arguments it can be directly passed
# If i have dictionary it has to be in ** format

# Combination of *args & **kwargs
# Non-Keyword Arguments First and Keyword Arguments Second
def Combination(*args,**kwargs):
    sum = 0
    for i in args:
        sum = i + sum
    print(sum)
    for k,v in kwargs.items():
        print(k,v)

# t = [1,2,3,5,6,7,8,12,32]
# key_arg = {'a':'1','b':'2'}
# Combination(1,2,3,4,a=1,b=2,c=3)
# Combination(*t,**key_arg)


# Nested Function
def outer():
    def inner():
        print('Inner Function')
    return inner

a = outer()
a()

# Two things --- Returned as Reference and returned as execution Type
# Though my Initial Outer or Main Function has ended and my variables/memory are flushed.
# we can still remember the inside function using Reference Return Type

# Closures --> Even though My function seizes out, I remember something from my function which is called as Closures
# So thing in this case, 'a' is Closure

print(summation1.__name__)