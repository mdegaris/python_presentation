# from functools32 import lru_cache


# Recursive Fibonacci sequence
# @lru_cache(maxsize=10)
def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))


for i in range(38):
    f = fib(i)
    print('{}: {}'.format(str(i), str(f)))
