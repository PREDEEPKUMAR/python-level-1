import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        value = func(*args, **kwargs)
        # Functions or Codes inside
        return value
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


@my_decorator
def say_hi():
    print("Hiii!")


@my_decorator
def greet(name):
    print("Welcome ",name)
    return 'Good Luck!'

# result = my_decorator(say_wow)
# result()

# say_whee()
# returned = greet('Divyam')
# print(returned)
# say_hi()


# print(greet.__name__)

# Here say_whee or say_hi or say_wow --- Decorated Function ( Special behaviour or other funtions to this Funtion)
# Decorator -- Something which returns the reference
# Using @ symbol, I Can easily call my decorator

# Use case for Decorator
from datetime import datetime
import time


def not_during_the_night(func):
    def wrapper(*args,**kwargs):
        if 7 <= datetime.now().hour < 22:
            func(*args,*kwargs)
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
@not_during_the_night
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
    print('Morning Buddy')


waste_some_time(10)
