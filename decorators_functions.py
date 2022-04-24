def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner


@decorator_list
def add_together(a, b):
    return a + b

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

# Small exercises - 1

import datetime

def log(func):
    def wrapper(*args):
        f = open('log.txt', 'a+')
        f.write(f'{datetime.datetime.now()}, {args}, {func(*args)}\n')
        return func(*args)
    return wrapper

@log
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

@log
def printer(text):
    print('From printer')


# Ex1: Time it!

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = (time.time()) - start
        print(f'Time elapsed: {end}')

    return wrapper

@timer
def genrate_list(num):
    [x for x in range(1, num)]

# Ex3: Slow down code

"""
    Exercise: Slow down code

    The code below counts down from n -> 0.
    calling countdown(5) prints: 5 4 3 2 1 0

    Create a decorator that slows down you code by 1 second for each step. 
    Call it slowdown().
    For this you can use the 'time' module.

    The countdown function is a recursive function.

    When you got the 'slowdown code' working on this recursive function, try to create a more (for you) normal function that does the countdown, and see what happens if you decorate that function with you slowdown() function

"""

import time


def slowdown(func):
    def wrapper(n):
        time.sleep(1)
        return func(n)

    return wrapper


@slowdown
def countdown(n):
    if not n:  # 0 is false, not false is true
        print('liftoff')
    else:
        print(n)
        return countdown(n - 1)  # call the same function with n as one less