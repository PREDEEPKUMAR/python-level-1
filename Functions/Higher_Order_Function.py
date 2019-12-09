# # Code for Higher Order Function to call Func as argument
def car(b=10):
    print('Car is called')
    return b


def execute(func,*args):
    c = func(*args)
    return c
#
execute(car,20)
#
# # Higher Order Function as Return Type
def add_tw0_nums(x, y): # normal function which returns data
    return x + y
#
def add_three_nums(x, y, z): # normal function which returns data
    return x + y + z
#
def get_appropriate_function(num_len): # function which returns functions depending on the logic
    if num_len == 3:
        return add_three_nums
    else:
        return add_tw0_nums
#
#
a = [1,2,3]
res_func = get_appropriate_function(len(a))
print(res_func(*a))


# USE CASE
# OLD CODE
def sum_naturals(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_sqaures(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k, k + 1
    return total

def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k *k, k + 1
    return total

def pi_sum(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + 8 / ((4 * k - 3) * (4 * k - 1)), k + 1
    return total

# Modified Code with Higher Order Function as Concept
# HIGHER ORDER -- Use func name as arg or return my func name as arg
def sum_naturals(n, func):
    total, k = 0, 1
    while k <= n:
        total, k = total + func(k), k + 1

    return total

def identity(x):
    return x

def square(x):
    return x * x

def cube(x):
    return x * x * x

def pi_term(x):
    return 8 / ((4 * x - 3) * (4 * x - 1))

def action(n, operation):
    return sum_naturals(n, operation)

n = 10
print(action(n, identity))
print(action(n, square))
print(action(n, cube))
print(action(n, pi_term))
