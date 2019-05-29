from memory_profiler import *
import random

@profile(precision=4)
def test():
    a = [random.randint(1, 100) for _ in range(100000)]
    b = set(a)


if __name__ == '__main__':
    test()
