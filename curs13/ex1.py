# 1. Create a decorator function that will execute function 3 times.


def x3(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper

@x3
def sum_one_million():
    s = 0
    for i in range(10000):
        s += i
    print(s)

sum_one_million()