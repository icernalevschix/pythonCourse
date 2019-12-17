# 3. Write a decorator for division function
# In case of ZeroDivisionError print a message that Division by 0 is not allowed.

def zero_divisor_decorator(func):
    def wrapper(*args):
        try:
            res = func(*args)
        except ZeroDivisionError:
            print("Division by 0 is not allowed")
            return False
        else:
            return res

    return wrapper

@zero_divisor_decorator
def divisor_function(number, divisor):
    return number / divisor

print(divisor_function(100,0))