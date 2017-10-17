from inspect import isgeneratorfunction
__author__ = 'woody'


def fib_senior(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1

def fib_return_list(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n += 1
    return L

def fib_with_yield(max):

    """
    this is a doc example
    :param max:
    :return:
    """
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1

print(isgeneratorfunction(fib_with_yield))

for n in fib_with_yield(5):
    print(n)


print(len(dir([])),len([x for x in dir([]) if not x.startswith("__")]))
print([a for a in dir(list) if not a.startswith("__")])

def dir1(x): return [a for a in dir(x) if not a.startswith("__")]

print(dir1(list))
print(dir1(tuple))
print(dir1(dict))
print(dir1(set))
print(fib_with_yield.__doc__)
help(list)
