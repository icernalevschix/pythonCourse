# 2. Consider following function ... Write a decorator function that will calculate function execution time.
## 1. Write a decorator that will print functions name and it’s attributes on call. Use func.__name__ attribute
### 2. Create a decorator that will repeat function execution N times with X seconds delay. Use time.sleep() function.

import time

def repeat(n, delay):

    def execution_time(func):

        def wrapper(*args):
            print('*args = ', *args)
            print('func name =', func.__name__)
            start = time.time()
            for i in range(n):
                print(func(*args))
                time.sleep(delay)
            end = time.time()
            print('execution time:' , end - start)

        return wrapper

    return execution_time

@repeat(3, 0.5)
def sum_one_million(nr):
    s = sum((i for i in range(nr)))
    return s

sum_one_million(100000)

