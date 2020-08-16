import time

from functools import lru_cache


@lru_cache()
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


n1 = 100


def test(n):
    # start = time.time()
    for i in range(1, 1000):  # checking the rate of growth for fun
        print(fibonacci(i + 1) / fibonacci(i))

    ''' this gives the golden ratio'''
    # print(str(time.time()- start) + ' seconds') remove # to check time


test(n1)

'''
Previous attempt

fibo_cache = {}
def fibonacci(n):
    if n in fibo_cache:
        return fibo_cache[n]
    if n in [0, 1]:
        return n
    else:
        val = fibonacci(n - 1) + fibonacci(n - 2)
    fibo_cache[n] = val
    return val

n1 = 50 result is 12586269025 and took >5min for the code wars sample code
n1 = 100 for this function took 0.0006 seconds in average, same as the answer above.
'''
