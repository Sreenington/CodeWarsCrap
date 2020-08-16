import time

from functools import lru_cache

fibo_cache = {}


# BEST APPROACH (requires module). Avg. Time: 4481ms
@lru_cache(maxsize=None)
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# 2ND APPROACH. Avg. Time: 4745ms
def fibonacci(n):
    if n in fibo_cache:
        return fibo_cache[n]
    if n in [0, 1]:
        return n
    val = fibonacci(n - 1) + fibonacci(n - 2)
    fibo_cache[n] = val
    return val


# 3RD method Best. Avg. Time: 4965ms
def fibo(n):
    f = [0, 1]
    if n in fibo_cache:
        return fibo_cache[n]
    for i in range(2, n + 1):
        (f.append(f[-1] + f[-2]))
    fibo_cache[n] = f[n]
    print(fibo_cache)
    return print(f[n])


n1 = 100


def test(n):
    start = time.time()
    fibo(n1)
    print(str((time.time()) - start) + ' seconds')
    # fibonacci(n1)
    # print(str((time.time()) - start) + ' seconds')
    '''for i in range(1, 1000):  # checking the rate of growth for fun
        print(fibonacci(i + 1) / fibonacci(i))
     this gives the golden ratio'''
test(n1)

'''
Previous attempt

fibo_cache = {}
def fibonacci(n):
    if n in fibo_cache:
        return fibo_cache[n]
    if n in [0, 1]:
        return n
    val = fibonacci(n - 1) + fibonacci(n - 2)
    fibo_cache[n] = val
    return val

n1 = 50 result is 12586269025 and took >5min with the code wars sample code
n1 = 100 for this function took 0.0006 seconds in average, same as the answer above.
'''
