import time
import random

from collections import defaultdict, deque, namedtuple, Counter


def deque_vs_list_example():
    a = list(range(1000000))
    start = time.time()
    for i in range(1000):
        a.append(i)
        a.pop(0)
    print("usando lista {}".format(time.time() - start))
    a = deque(range(1000000))
    start = time.time()
    for i in range(1000):
        a.append(i)
        a.popleft()
    print("usando deque {}".format(time.time() - start))


def namedtuple_example():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(2, y=4)
    print(p.x + p.y)


def counter_example():
    numbers = [random.randint(1,10) for i in range(50)]
    c = {}
    for n in numbers:
        if n in c:
            c[n] += 1
        else:
            c[n] = 1
    print(c)
    # o cast aqui é só para ordenação
    print(dict(Counter(numbers)))
