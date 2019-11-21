a = lambda x: x + 1
print(a(1))
b = (lambda x, y: x + y)(2,3)
print(b)

action = {
        "1": lambda x: x + 1,
        "2": lambda x: x + 2,
        "3": lambda x: x + 3
    }

r = action["3"](1)
print(r)

def f1(x): return x + 1
def f2(x): return x + 2
def f3(x): return x + 3
action = {"1": f1, "2": f2, "3": f3}
print(action["1"](1))

# map

