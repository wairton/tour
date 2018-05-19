from functools import singledispatch, wraps, partial


def singledispatch_example():
    @singledispatch
    def magic(value, message="{}"):
        print("magic for all other types")
        print(message.format(value))

    @magic.register(int)
    def _(value, message="{}"):
        print("magic for ints")
        print(message.format(value + value))

    @magic.register(list)
    def _(value, message="{}"):
        print("magic for lists")
        print(message.format(value[0]))

    magic(3)
    magic([2, 3])
    magic(4.5)


def wraps_example():
    def decorator1(func):
        def wrapper():
            print("magic")
            func()
        return wrapper

    @decorator1
    def foo():
        "amazing docs"
        print("foo")

    print("*** sem wraps ***")
    foo()
    print(foo.__name__)
    print(foo.__doc__)

    def decorator2(func):
        @wraps(func)
        def wrapper():
            print("magic")
            func()
        return wrapper

    @decorator2
    def foo():
        "amazing docs"
        print("foo")

    print("*** com wraps ***")
    foo()
    print(foo.__name__)
    print(foo.__doc__)


def partial_example():
    def soma(a, b):
        return a + b

    soma3 = partial(soma, b=3)
    print(soma3(3))

