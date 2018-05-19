import math
import time
from multiprocessing import Pool

def f(x):
    return math.exp(x % 100) * math.log(x)


ITERATIONS = int(1E7)

s = time.time()
for i in range(1, ITERATIONS):
    f(i)
print("sequential: {}".format(time.time() - s))
time.sleep(2)
s = time.time()
with Pool(processes=4) as pool:
    pool.map(f, range(1, ITERATIONS))
print("parallel: {}".format(time.time() - s))

